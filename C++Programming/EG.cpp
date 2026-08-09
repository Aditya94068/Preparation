#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int binarySearch(vector<int>arr,int target){
    int start  = 0;
    int end = arr.size() - 1;
    int mid = start + (end - start)/2;
    while(start<=end){
        if(arr[mid] == target){
            return mid;
        }
        else if(arr[mid] > target){
            end = mid - 1;
        }
        else {
            start = mid + 1;
        }
        mid = start + (end - start)/2;
    }
    return -1;
}
int firstOccurancce(vector<int>arr , int target){
    int start = 0;
    int end = arr.size() -1;
    int mid = start + ( end  - start )/2;
    int ans = -1;
    while(start<=end){
        if(arr[mid] == target){
            ans = mid;
            end  = mid -1;
        }
        else if(arr[mid]<target)
        {
            start = mid + 1;
        }
        else if(arr[mid]>target){
            end = mid -1;
        }
        mid = start + (end - start)/2;
    }
    return ans;
}

int lastOccurance(vector<int>arr , int target){
    int start = 0;
    int end = arr.size() - 1;
    int mid = start + (end - start)/2;
    int ans = -1;
    while(start<=end){
        if(arr[mid] == target){
            ans  = mid;
            start = mid  + 1;
        }
        else if(arr[mid]>target){
            end = mid - 1;
        }
        else if(arr[mid] < target){
            start = mid + 1;
        }
        mid = start + (end - start)/2;
    }
    return ans;
}

int FindMissingNumber(vector<int>nums){
   int start = 0;
   int end = nums.size() -1;
   int mid = start + (end - start)/2;
   while(start<=end){
    if(nums[mid] == mid + 1){
        start = mid  +1;
    }
    else if(nums[mid] != mid + 1)
    {
        end = mid -1;
    }
    mid = start + (end - start)/2;
   }
   return start + 1;
}
int main(){
    // vector<int>arr {1,2,3,4,5,60};
    // int target = 4;
    // int TargetElementIndex  = binarySearch(arr,target);

    // cout<<TargetElementIndex<<endl;

    // if(binary_search(arr.begin(),arr.end(),target)){
    //     cout<<"found"<<endl;
    // }
    // else {
    //     cout<<"Not Found"<<endl;
    // }

    // int ARRAY[] = {1,2,3,4,5,6};
    // int n = 6;
    // int t = 54;
    // if(binary_search(ARRAY,ARRAY + 6 ,t)){
    //     cout<<"found"<<endl;
    // }
    // else {
    //     cout<<"Not Found"<<endl;
    // }

    // vector<int>arr {1,2,3,3,3,4,4,4,4,4,4,5,5,6,7};
    // int indexFirstOcc = firstOccurancce(arr,3);
    // cout<<indexFirstOcc<<endl;
    
    
    // // vector<int>arr {1,2,3,3,3,3,4,5,5,6,7};
    // int indexLastOcc = lastOccurance(arr,3);
    // cout<<indexLastOcc<<endl;


    // int totaloccurance = indexLastOcc - indexFirstOcc + 1;
    // cout<<totaloccurance<<endl;


    // //stl function for occurance
    // int target = 3;
    // auto ans1 = lower_bound(arr.begin(),arr.end(),target);
    // cout<<"Ans = "<<ans1 - arr.begin()<<endl;

    // int t = 4;
    // auto ans2 = upper_bound(arr.begin(),arr.end(),t);
    // cout<<"Ans = "<<ans2 - arr.begin() -1<<endl;


    vector<int>arr = {2,3,4,5,6,7};
    int ans = FindMissingNumber(arr);
    cout<<ans;
    return 0;
}