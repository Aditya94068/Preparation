#include<iostream>
#include<vector>
#include<climits>
using namespace std; 
int findkRotation(vector<int>arr){
    int low = 0;
    int high = arr.size()-1;
    int ans = INT_MAX;
    int index = -1;
    while(low <= high){
        int mid  = low  + (high - low) /2;
        if(arr[low] <= arr[high]){
            if(arr[low] < ans){
                ans = arr[low];
                index = low;
            }
            break;
        }
        if(arr[low] <= arr[mid]){
            if(arr[low] < ans){
                ans = arr[low];
                index = low;
            }
            low = mid + 1;
        }
        else {
            high = mid - 1;
            if(arr[mid] < ans){
                ans = arr[mid] ;
                index = mid ;
            }
        }
    }
    return index;
}
int main(){ 
    vector<int>arr = {4,1,2,3};
    int ans = findkRotation(arr);
    cout<<ans<<endl;
    return 0;
}