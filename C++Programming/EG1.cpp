#include<iostream>
using namespace std;
void function(int arr[],int n,int i){
    if(arr[i] >=n/2){
        return ;
    }
    swap(arr[0],arr[n-i-1]);
    function(arr,n,i+1);
}

bool Palidroem(char arr[],int n,int i){
    if(i>=n/2){
        return true;
    }
    if(arr[i] !=arr[n-i-1]){
        return false;
    }
    return Palidroem(arr,n,n+1);
}
int FibonacciSeries(int n){
    if(n<=1){
        return n;
    }
    int last = FibonacciSeries(n-1);
    int slast =FibonacciSeries(n-2);
    return last + slast;
    }

int main(){
    int arr[] ={1,2,3,4,5};
    int n= sizeof(arr)/sizeof(arr[0]);
    function(arr,n,0);
    for(int i = 0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    char a[] = {'M','A','D','A','M'};
    int  m =sizeof(a)/sizeof(a[0]);
    cout<<Palidroem(a,m,0)<<endl;


    cout<<FibonacciSeries(4)<<endl;
    return 0;
}