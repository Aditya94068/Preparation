#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
void SubSequence(vector<int>&arr,vector<int> &ans ,int n ,int i){
    if(i>=n){
        for(int it : ans){

            cout<<it<<" ";
        }
        if(ans.size() == 0){
            cout<<"{ }";
        }
        cout<<endl;
        return ;
    }
    ans.push_back(arr[i]);
    SubSequence(arr,ans,n,i+1);
    ans.pop_back();
    SubSequence(arr,ans,n,i+1);
}
int main(){
   vector<int>arr {3,1,2};
    int n = arr.size();
    vector<int>ans;
    SubSequence(arr,ans,n,0);
   
    return 0;
}