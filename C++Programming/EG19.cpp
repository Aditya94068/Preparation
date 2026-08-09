#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int binarySearch(int arr[],int size,int target){
    int start = 0;
    int end = size -1 ;
    int mid = start  + (end - start)/2;
    while(start<=end){
        int element = arr[mid];
        if(element == target){
            return mid;
        }
        //left
        else if(element < target){
          start = mid + 1;
        }
        //Right
        else if(element >target) {
            end = mid -1;
        }
          mid = start  + (end - start)/2;

    }
    return -1;
}
int main(){
    // int arr[] = {2,4,7,10,15,19,21};
    // int target = 19;
    // int size = 7;
    // int targetIndex = binarySearch(arr,size,target);
    // if(targetIndex == -1){
    //     cout<<"Not Found "<<endl;
    // }
    // else{
    //     cout<<"Target Found At "<<targetIndex<<" Index"<<endl;
    // }

    // vector<int>v{1,2,3,4,5};
    // if(binary_search(v.begin(),v.end(),4)){
    //     cout<<"Found"<<endl;
    // }
    // else{
    //     cout<<"Not Found"<<endl;
    // }

    int arr[] = {1,2,3,4,5,6,7};
    int size = 7;
    if(binary_search(arr,arr+size,53)){
        cout<<"Found"<<endl;
    }
    else {
        cout<<"Not Found"<<endl;
    }
    return 0;
}