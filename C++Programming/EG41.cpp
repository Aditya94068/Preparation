#include<bits/stdc++.h>
using namespace std;
int findFunction(vector<int>& arr,int n ,int k){
        int i = 0;
        for(int i = 0;i<arr.size();i++){
            if(arr[i] == k){
                return i;
            }
        }
        return -1;
}
vector<int>eraseFunction(vector<int>& arr,int n ,int k){
      int i =0;
      vector<int>ans;
      for(int i = 0;i<arr.size();i++){
            if(arr[i] == k){
                continue;
            }
            
            else{
                ans.push_back(arr[i]);
            }
      }
      return ans;
}
int main(){
    vector<int>arr = {10,20,30,50};
    int n = arr.size();
    int ans = findFunction(arr,n,390);
    cout<<ans<<endl;
    vector<int>ans_v = eraseFunction(arr,n,40);
    for(auto val : ans_v){
        cout<<val<<" ";
    }
    return 0;
}