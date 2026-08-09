#include<iostream>
#include<vector>
using namespace std;
int lowerBound(vector<int>arr,int x){
    int low = 0;
    int high = arr.size() - 1;
    int ans = -1;
    while(low <= high){
        int mid = (low + high)/2;
        if(arr[mid] >= x){
            ans = mid;
            high = mid - 1;
        }
        else {
            low = mid  + 1;
        }
    }
    return ans;
}

int upperBound(vector<int>arr,int x){
    int low = 0;
    int high = arr.size() - 1;
    int ans = -1;
    while(low <= high){
        int mid = (low + high)/2;
        if(arr[mid] > x){
            ans = mid;
            high = mid - 1;
        }
        else {
            low = mid  + 1;
        }
    }
    return ans;
}
vector<int>find_range(vector<int>arr,int x){
    vector<int>ans;
    int n = arr.size();
    int lb = lowerBound(arr,x);
    int ub = upperBound(arr,x);
    cout<<arr[lb]<<","<<arr[ub] <<endl;   
    if(lb == n || arr[lb] != x){
        ans.push_back(-1);
        ans.push_back(-1);
    }
    else{
        ans.push_back(lb);
        ans.push_back(ub);
    }
        return ans;
}
int main(){
    vector<int>arr = {2,4,6,8,8,8,8,11,13};
    vector<int>ans = find_range(arr,10);
    cout<<endl;
    for(auto val:ans){
        cout<<val<<endl;
    }
    return 0;
}