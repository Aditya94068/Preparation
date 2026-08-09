#include<bits/stdc++.h>
using namespace std;
vector<int> ZerosAndOnes(vector<int>& arr){
    int i = 0;
    int j = arr.size()-1;
    while(i<j){
        if(arr[i] == 0){
            i++;
        }
        else if(arr[i]==1){
            swap(arr[i],arr[j]);
            j--;
        }
    }
    return arr;
}
int main(){
    // vector<int> arr {1,1,0,1,1,1,0,0,1,1,0,0,0};
    // vector<int>ans = ZerosAndOnes(arr);
    // for(auto val : ans){
    //     cout<<val<<" ";
    // }
    // cout<<endl;
    // cout<<"fasfa"<<endl;
    // cout<<12/10<<endl;

    int i = 1202;
    int ans = 0;
    while(i>0)
    {
        int digit = i % 10;
        ans = ans * 10 + digit;
        i = i / 10;
    }
    cout<<ans<<endl;
    return 0;
}