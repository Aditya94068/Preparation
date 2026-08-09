#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<int>Factorial(int n){
    // vector<int>ans;
    // int carry = 0;
    // ans.push_back(1);
    
    // for(int i = 2;i<=n;i++){
    //    for(int j = 0;j<ans.size();j++){
    //       int x = ans[j] * i + carry;
    //       ans[j] = x % 10;
    //       carry = x / 10;
    //    }
    //     while(carry){
    //         ans.push_back(carry);
    //         carry = carry/10;
    //     }
    // }
    // reverse(ans.begin(),ans.end());
    // return ans;

    vector<int>ans;
    ans.push_back(1);
    int carry = 0;
    for(int i = 2;i<=n;i++){
        for(int j =0;j<ans.size();j++){
            int x = ans[j] * i + carry;
            ans[j] = x % 10;
            carry = x /10;
        }
        while(carry){
            int y = carry%10;
            ans.push_back(y);
            carry /=10;
        }
    }
    reverse(ans.begin(),ans.end());
    return ans;
}

int main(){
   
    int n = 50;
    vector<int> ans = Factorial(n);

    // cout<<60/10<<endl;
    for(auto val : ans){
        cout<<val<<" ";
    }
    return 0;
}