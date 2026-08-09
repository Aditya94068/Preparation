#include<iostream>
#include<vector>
using namespace std;
vector<int> PlusOne(vector<int>& digits){
     int n = digits.size()-1;
     for(int i = n;i>=0;i--){
        if(digits[i]==9){
            digits[i] = 0;
        }
        else{
            digits[i] +=1;
            return digits;
        }
     }
     digits.push_back(0);
     digits[0] = 1;
     return digits;
}
int main(){
    vector<int> arr {3,9,9};
    vector<int>ans = PlusOne(arr);
    for(int val : ans){
        cout<<val<<" ";
    }
    // vector<int>arr{1,2,3};
    // // cout<<arr.size()<<endl;
    // cout<<(2^1)<<endl;
    return 0;
}