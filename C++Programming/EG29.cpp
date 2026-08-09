#include<iostream>
#include<vector>
using namespace std;

int binarySearch(int arr[],int start,int end ,int x){
     while(start<=end){
        int mid = start + (end - start)/2;
         if(arr[mid] == x)
         return mid;
         else if(arr[mid] > x)
         end = mid -1;
         else {
            start = mid + 1;
         }
     }
     return -1;
}
int expSearch(int a[] , int n,int x){
    if(a[0] == x) return 0;
    int i = 1;
    while(i<n && a[i] <=x){
        i = i * 2;
    }
    return binarySearch(a,i/2,min(i,n-1),x);
}
int infiniteLinearSearch(int arr[],int x){
    int i = 0;
    int ans = -1;
    while(1){
        if(arr[i] > x){
            break;
        }
        if(arr[i] == x){
            ans = i;
        }
        i++;
    }
    return ans;
}
int unbounded_search(int arr[] , int k ){
    int i = 0;
    int j = 1;
    while(arr[j]  < k){
            i = j;
            j = j * 2;
    }
    return binarySearch(arr,i,j,k);
}
int main(){
    int a[] ={3,4,5,6,11,13,14,15,56,70};
    vector<long>arr;
   

    int n = sizeof(a)/sizeof(a[0]);
    int x = 56;
    int ans = expSearch(a,n,x);
    cout<<ans<<endl;
    int result = infiniteLinearSearch(a,x);
    cout<<result<<endl;

    cout<<unbounded_search(a ,x)<<endl;
    return 0;
}