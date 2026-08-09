#include<iostream>
#include<climits>
#include<bits/stdc++.h>
using namespace std;
// void  printcount(int n)
// {
//      if(n == 0) return ;
//     int digit = n % 10;
//     printcount(n/10);
//     cout<<digit<<endl;
       
// }
// void array(int arr[],int n , int i){
//     if(i >=n){
//         return ;
//     }
//     cout<<arr[i]<<" ";
//     array(arr,n,i+1);
// }
void  maxiNumber(int arr[] ,int n ,int i , int& maxi)
{
    if(i >= n)
    {
        return ;
    }
    if(maxi < arr[i])
    {
        maxi = arr[i];
    }
     maxiNumber(arr,n , i + 1,maxi);
}
void minNumber(int nums[] ,int n , int i , int& mini)
{
    if(i == n)
    {
        return ;
    }
    if(nums[i] < mini)
    {
        mini = nums[i];
    }
    minNumber(nums,n,i + 1,mini);
}
void  isCharpresent(string& s,int i , int& n,char& key,int& count)
{
    if(i >= n) {
        return ;
    }
    if(s[i] == key){
       count = count + 1;
    }
    isCharpresent(s,i+1,n,key,count);
}
void printDigit(int n)
{
    if(n == 0)
    {
        return ;
    }
    int digit = n % 10;
    printDigit(n/10);
    cout<<digit<<" ";
}
int main()
{
//     string str = "love babbar";
//     int n = str.length();
//     int i = 0;
//     vector<int>arr;
//     char key = 'b';
//     int count = 0;
//     isCharpresent(str,i ,n,key,count);
//     cout<<count<<endl;
//     for(int i = 0;i<arr.size();i++)
//     {
//         cout<<arr[i]<<endl;
    // }

    int n = 0647;
    cout<<n<<endl; // 423 

    printDigit(n);
    // int arr[] = {11,20,9,45,242,42};
    // int n = 6;
    // int i = 0;
    // int maxi = INT_MIN;
    // maxiNumber(arr,n,i,maxi);
    // cout<<maxi<<endl;
    // int mini = INT_MAX;
    // minNumber(arr,n,i,mini);
    // cout<<mini<<endl;


    // int n ;
    // cout<<"Enter a number :"<<endl;
    // cin>>n;
    // int ans = printcount(n);
    // printcount(n);
    // cout<<ans;
    // int arr[5] = {10,20,30,40,50};
    // int n = 5;
    // int i = 0;
    // array(arr,n,i);
    return 0;
}