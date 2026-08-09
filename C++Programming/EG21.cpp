#include<iostream>
#include<vector>
using namespace std;
int FindMissingNumber(vector<int>arr){
    int start = 0;
    int end = arr.size() -1;
    int mid  = start + (end  - start ) / 2;
    while(start <= end)
    {
        if(arr[mid] == mid + 1){
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
        mid = start + (end - start)/2;
    }
    return mid  + 1;
}
int main(){
    vector<int>arr{1,2,3,5,6};
    int missingElement = FindMissingNumber(arr);
    cout<<missingElement<<endl;
    return 0;
}