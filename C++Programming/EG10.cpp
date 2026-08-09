#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int findduplicate(vector<int>& arr){
    // sort(arr.begin(),arr.end());
    // for(int i = 0;i<arr.size();i++){
    //     if(arr[i] == arr[i+1]) return arr[i];
    // }

    // int ans = -1;
    // for(int i =0;i<arr.size();i++){
    //     int index = abs(arr[i]);
    //     if(arr[index]<0){
    //         ans = index;
    //         break;
    //     }
    //     arr[index] = arr[index]*-1;
    // }
    // return ans;

    // int ans = -1;
    // for(int i = 0;i<arr.size();i++){
    //     int index = abs(arr[i]);
    //     if(arr[index]<0){
    //         ans = index;
    //         break;
    //     }
    //     arr[index ] *=-1;
    // }
    // return ans;


    // while(arr[0] !=arr[arr[0]])
    // {
    //     swap(arr[0],arr[arr[0]]);
    // }
    // return arr[0];

    while(arr[0]!=arr[arr[0]]){
        swap(arr[0],arr[arr[0]]);
    }
    return arr[0];
}
int main(){
    vector<int> arr {1,2,2,4,3};
    int ans = findduplicate(arr);
    cout<<ans;
    return 0;
}