#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int firstOccurance(vector<int>arr,int target){
    int start = 0;
    int end = arr.size()-1;
    int ans = -1;
    int mid  = start + (end - start)/2;
    while(start<=end){
        if(arr[mid] == target){
            ans  = mid;
            end = mid - 1;
        }
        else if(target < arr[mid]){
            end = mid - 1;
        }
        else if(target > arr[mid]){
             start = mid +  1;
        }
        mid = start + (end - start)/2;
    }   
    return ans;
}
int lastOccurance(vector<int>arr,int target){
    int start = 0;
    int end = arr.size()-1;
    int ans = -1;
    int mid = start + (end - start)/2;
    while(start<=end){
        if(arr[mid] == target){
            ans = mid ;
            start = mid + 1;
        }
        else if(target < arr[mid]){
            end = mid -1;
        }
        else if(target >arr[mid]){
            start = mid + 1;
        }
        mid = start + (end - start )/2;
    }
    return ans;
} 
int main(){

    vector<int>arr = {1,3,4,4,4,4,4,4,4,4,4,4,6,7};
    int target = 4;
    int firstOccuranceIndex = firstOccurance(arr,target);
    cout<<firstOccuranceIndex<<endl;
    int lastOccuranceIndex = lastOccurance(arr,target);
    cout<<lastOccuranceIndex<<endl;
    cout<< lastOccuranceIndex - firstOccuranceIndex + 1<<endl;


    // auto ans = lower_bound(arr.begin(),arr.end(),target);
    // cout<<"ans = "<<ans - arr.begin()<<endl;
    // auto ans1 = upper_bound(arr.begin(),arr.end(),target);
    // cout<<"ans = "<<ans1 - arr.begin()<<endl;
    return 0;
}