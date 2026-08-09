#include<iostream>
#include<vector>
using namespace std;
int PivotElement(vector<int>arr){
    int start = 0;
    int end = arr.size()-1;
    int mid = start + (end - start)/2;
    while(start<=end){
        if(start == end){
            return mid;
        }
        if(mid + 1<=end && arr[mid + 1]<arr[mid]){
            return mid;
        }
        if(mid - 1>=start && arr[mid - 1] > arr[mid]){
            return mid - 1;
        }
        if(arr[start] > arr[mid]){
            end =  mid -1;
        }else {
            start = mid + 1;
        }
        mid = start + (end - start)/2;
    }
    return -1;
}
int main(){
    vector<int>arr{1,2,3};
    int ans = PivotElement(arr);
    cout<<"Ans at Index = "<<ans<<endl;
    cout<<"Index on Ans = "<<arr[ans]<<endl;
    return 0;
}