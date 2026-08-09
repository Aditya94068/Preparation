#include<bits/stdc++.h>
using namespace std;
class info{
    public:
    int data;
    int row ;
    int col ;
    info(int data , int row , int col ){
        this->data = data;
        this->row = row;
        this->col = col;
    }
};  
class compare{
    public:
    bool operator()(info* a, info* b)
    {
        return a->data > b->data;
    }
};
vector<int>mergeKSortedArray(int arr[][3],int k, int n)
{  
    priority_queue<info*,vector<info*>,compare>minHeap;
    for(int i = 0;i<k;i++)
    {
        info* temp = new info(arr[i][0],i,0);
        minHeap.push(temp);
    }
    vector<int>ans;
    while(!minHeap.empty())
    {
        info* temp = minHeap.top();
        int topData = temp->data;
        int toprow = temp->row;
        int topcol = temp->col;
        ans.push_back(topData);
        minHeap.pop();
        if(topcol + 1 < n)
        {
            info* temp = new info(arr[toprow][topcol + 1],toprow, topcol + 1);
            minHeap.push(temp);
        }
    }
    return ans;
}
int main()
{
    int arr[][3] = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    int n = 3;
    
    vector<int>ans = mergeKSortedArray(arr,k,n);
    for(int i = 0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
    return 0;
}