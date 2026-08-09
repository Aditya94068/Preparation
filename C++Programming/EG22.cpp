#include<iostream>
#include<vector>
using namespace std;
int PivotElement(vector<int>arr){
    int start =0;
    int end = arr.size() -1;
    int mid = start + (end - start)/2;
    while(start<end){
        if(arr[mid] < arr[mid  + 1]){
            start = mid + 1;
        }
        else {
            end = mid;
        }
        mid = start + (end - start)/2;
      
    }
    return end;
}

int main(){
    vector<int>arr = {6,7,1,2,3,4,5};
    int ans = PivotElement(arr);
    cout<<ans;
    
    return 0;   
}