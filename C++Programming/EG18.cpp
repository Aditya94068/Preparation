#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;

int main(){
    vector<int>arr = {3,2,1};
    sort(arr.begin(),arr.end() ,greater<int>());
    for(int val : arr){
        cout<<val<<" ";
    }
    return 0;
}