#include<iostream>
#include<vector>
using namespace std;
bool PrintSum(int i, int s,int arr[],int n ,int sum ,vector<int>&ds){
    if(i == n)
    {
        if(sum == s){
            for(auto it: ds ){
                cout<<it<<" ";
            }
            cout<<endl;
            return true;
        }
        else return  false;
    }
    ds.push_back(arr[i]);
    s= s + arr[i];
    if(PrintSum(i+1,s,arr,n,sum,ds) == true){
        return true;
    }
    s = s- arr[i];
    ds.pop_back();
    if(PrintSum(i+1,s,arr,n,sum,ds) == true){
        return true;
    }
    return false;
    
}
int main(){
    int arr[] = {1,2,1};
    int n = 3;
    int sum = 2;
    vector<int>ds;
    PrintSum (0 ,0,arr,n,sum,ds);

    return 0;
}