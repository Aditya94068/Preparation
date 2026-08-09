#include<iostream>
#include<vector>
using namespace std;
int BinarySearch(vector<int>arr,int target){
    int start =0;
    int end = arr.size()-1;
    int mid = start + (end - start)/2;
    while(start<=end){
        if(arr[mid] == target){
            return mid;
        }
        if(mid - 1>=start && arr[mid - 1] == target)
        {
            return mid -1;
        }
        if(mid  + 1<= end && arr[mid + 1] == target){
            return mid +1;
        }
        else if(arr[mid] > target){
            end =mid - 2;
        }
        else if(arr[mid]<target){
            start = mid + 2;
        }
        mid =start + (end -start)/2;
    }
    return -1;
}
int main(){
    vector<int>arr = {6,3,2,5,1,8,4};
    int target = 6;
    int ans = BinarySearch(arr,target);
    cout<<"Index of "<<target<<":"<<ans<<endl;
    return 0;
}