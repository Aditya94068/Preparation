#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    // int a ,b;
    // a = 2;
    // b = 2;
    // cout<<a%b<<endl;
    // string s = "abcdefg";
    // cout<<s.substr(0,5)<<endl;
    // string    str1 = date.substr(0,4);
    // string    str2 = date.substr(5,2);
    // string    str3 = date.substr(8,2);
    // // cout<<str1<<endl;
    // // cout<<str2<<endl;
    // // cout<<str3<<endl;
    
    
    // string  date = "2080-02-29";
    //     string str1 = date.substr(0,4);
    //     string str2 = date.substr(5,2);
    //     string str3 = date.substr(8,2);
    //     int num1 = stoi(str1);
    //     int num2 = stoi(str2);
    //     int num3 = stoi(str3);
    //     int sum1 = 0;
    //     while(num1>0){
    //         int digit = num1 % 2;
    //         sum1  =  sum1 * 10 + digit;
    //         num1 =  num1 / 2;
    //     }
    //     str1 = to_string(sum1);
    //     reverse(str1.begin(),str1.end());
    //     // cout<<sum1<<endl;
    //     int sum2 = 0;
    //     while(num2>0){
    //         int digit = num2 % 2;
    //         sum2  =  sum2 * 10 + digit;
    //         num2 =  num2/ 2;
    //     }
    //     str2 = to_string(sum2);
    //     reverse(str1.begin(),str1.end());
    //     // cout<<sum2<<endl;
    //     int sum3 = 0;
    //     while(num3>0){
    //         int digit = num3 % 2;
    //         sum3  =  sum3 * 10 + digit;
    //         num3 =  num3 / 2;
    //     }
    //     str3 = to_string(sum3);
    //     reverse(str3.begin(),str3.end());
    //     // cout<<str3<<endl;
    //     string ans = "";
    //     ans += str1 + "-" + str2 +"-" + str3;
    //     // cout<<ans<<endl;



    string s = "aditya";
    vector<int>storeSum;
    int sum = 0;
        for(int i = 0;i<s.size();i++)
        {
            // int num = s[i];
            // // cout<<num<<endl;
            // for(int j = i;j<=i;j++)
            // {
                
            //     sum = abs(sum - num);
            //     storeSum.push_back(sum);
            // }

             int num = s[i];
             storeSum.push_back(num);

        }
        
        // cout<<sum<<endl;
        for(int i = 0;i<storeSum.size();i++)
        {
            cout<<storeSum[i]<<endl;
        }
    return 0;
}