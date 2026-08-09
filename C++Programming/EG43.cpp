#include<bits/stdc++.h>
using namespace std;
int Binary_Search(vector<int>& arr,int n , int s , int e,int key)
{
    if(s > e) return -1;
    int mid = s + (e - s)/2;
    if(arr[mid] == key )
    {
        return mid;
    }
    if(arr[mid] <  key)
    {
        return Binary_Search(arr,n,mid + 1,e,key);
    }
    else{
        return Binary_Search(arr,n,s,mid - 1,key);
    }
}
int main()
{
    vector<int>arr = {10,20,30,40,50,60,70,80,90};
    int n = arr.size();
    int s = 0;
    int e = n - 1;
    int ans = Binary_Search(arr,n,s,e,40);
    cout<<ans<<endl;
    return 0;
}
