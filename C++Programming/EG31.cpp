#include<iostream>
#include<vector>
using namespace std;
// int lowerBound(vector<int>& arr ,int x){
//     int low = 0;
//     int high = arr.size()-1;
//     int ans = arr.size();
//     while(low <= high){
//         int mid = low + (high - low)/2;
//         if(arr[mid] >= x){
//             ans = mid;
//             high = mid -1;
//         }
//         else{
//             low = mid + 1;
//         }
//     }
//     return ans;
// }
int upperBound(vector<int>arr,int x){
    int low = 0;
    int high = arr.size()-1;
    int ans = arr.size();
    while(low<=high){
        int mid = low + (high - low)/2;
        if(arr[mid] > x){
            ans = mid;
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    return ans;
}
int main(){
    vector<int>arr = {1,2,3,3,7,8,9,9,11,12};
    int x = 9;
    // int ans = lowerBound(arr,x);
    // cout<<ans<<endl;
    int result = upperBound(arr,x);
    cout<<"Only through the function :"<<result<<endl;
    int p = lower_bound(arr.begin(),arr.end(),x) - arr.begin();
    cout<<"Using diresct fun :"<<p<<endl;
    int a[] =  {1,2,3,3,7,8,9,9,11,12};
    int n = sizeof(a)/sizeof(a[0]);
    int q = lower_bound(a,a+n,x)-a;
    cout<<q<<endl;
}