#include<iostream>
#include<vector>
using namespace std;
int PrintSum(int i, int s,int arr[],int n ,int sum ){
    if(i == n)
    {
        if(sum == s) return 1;

        else return 0;
    }
    
    s += arr[i];
    int l = PrintSum(i+1,s,arr,n,sum);

    s -= arr[i];

    int r = PrintSum(i+1,s,arr,n,sum); 
       
    return l + r;
    
}
int main(){
    int arr[] = {1,2,1};
    int n = 3;
    int sum = 2;
    vector<int>ds;
    cout<<PrintSum (0 ,0,arr,n,sum);

    return 0;
}