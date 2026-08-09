#include<bits/stdc++.h>
using namespace std;
int solve(vector<int>& arr,int target,int output){
    if(target == output)
    {
        return 0;
    }
    if(target < output)
    {
        return INT_MAX;
    }
    int mini = INT_MAX;
    for(int i = 0;i<arr.size();i++)
    {
        int ans  = solve(arr,target,output + arr[i]);
        if(ans != INT_MAX)
        mini = min(mini,ans + 1);
    }
    return mini;
}
int main()
{
    vector<int> arr = {1,2};
    int target = 5;
    int output = 0;
    int ans = solve(arr,target,output);
    cout<<"Answer :"<<ans<<endl;
}