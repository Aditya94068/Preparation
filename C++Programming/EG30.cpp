#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
bool isPossible(vector<int>arr,int sol,int k){
    int cnt = 0;
    int sum = 0;
    for(int i =0;i<arr.size();i++){
        if(arr[i] > sol){
            return false;
        }
        if(arr[i] + sum > sol){
            cnt++;
            sum = arr[i];
            if(cnt>=k){
                return false;
            }
        }
        else {
            sum +=arr[i];
        }
    }
    return true;
}
int findPages(vector<int>arr,int n,int k){
    int start =0;
    int sum = 0;
    for(int i =0;i<arr.size();i++){
        sum +=arr[i];
    }
    int end= sum;
    int ans =0;
    while(start<=end){
        int mid = start + (end -start)/2;
    
        if(isPossible(arr,mid,k)){
            ans = mid;
            end = mid -1;
        }
        else{
            start = mid  + 1;
        }
    }
    return ans;
}
int main(){
    vector<int>arr {12,34,67,90};
    int n = arr.size();
    int k = 2;
    int ans = findPages(arr,n,k);
    cout<<ans<<endl;

    return 0;
}