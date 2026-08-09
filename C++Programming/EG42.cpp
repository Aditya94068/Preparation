#include<iostream>
using namespace std;
bool issorted(int arr[] , int n , int i)
{
    if(i == n-1) {
        return true;
    }
    if(arr[i] > arr[i + 1])
    {
        return false;
    }
    return issorted(arr,n,i+1);
}
int main()
{
    int arr[] = {10,20,30,40,50,60};
    int n = 6;
    int i = 0;
    bool result = issorted(arr,n,i);
    if(result)
    {
        cout<<"Array is sorted"<<endl;
    }
    else{
        cout<<"Array is not sorted"<<endl;
    }
    return 0;
}