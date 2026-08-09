#include<iostream>
#include<algorithm>
using namespace std;
string Cal_Sum(int *a,int n ,int *b,int m){
    string ans;
    int i = n-1;
    int j = m-1;
    int carry = 0;
    while(i>=0 && j>=0){
        int x = a[i] + b[j] + carry;
        int digit = x % 10;
        ans.push_back(digit + '0');
        carry = x/10;
        i--,j--;
    }
    while(i>=0){
        int x = a[i] + 0 + carry;
        int digit = x % 10;
        ans.push_back(digit + '0');
        carry = x/10;
        i--;
    }
    while(j>=0){
        int x = 0 + b[j] + carry;
        int digit = x % 10;
        ans.push_back(digit + '0');
        carry = x/10;
        j--;
    }

    if(carry){
        ans.push_back(carry + '0');
    }
    while(ans[ans.size()-1]=='0')
    {
        ans.pop_back();
    }
    reverse(ans.begin(),ans.end());
    return ans;
}
int main(){
    int a[] ={0,9,0,0,3,5};
    int b[] = {2,2,7};
    string result = Cal_Sum(a,6,b,3);
    cout<<result<<endl;
    return 0;
}