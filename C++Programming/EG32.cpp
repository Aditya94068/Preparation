#include<iostream>
#include<climits>
#include<vector>
using namespace std;
int mini(vector<int>& arr){
    int miniNum = INT_MAX;
    for(int i =0;i<arr.size();i++){
        miniNum = min(miniNum,arr[i]);
    }
    return miniNum;
}
int maxi(vector<int>& arr){
    int maxNum = INT_MIN;
    for(int i =0;i<arr.size();i++){
        maxNum = max(maxNum,arr[i]);
    }
    return maxNum;
}
int solution(vector<int> &arr,int m){
    int sum = 0;
    int i ;
    int minii = mini(arr);
    int maxii = maxi(arr);
    int ans = 0;
    for(i = minii;i<=maxii;i++){
       
        long long sum = 0; // reset for each height

        for(int j = 0; j < arr.size(); j++){
            int x = arr[j] - i;
            if(x > 0)
                sum += x; // collect only positive wood
        }

        // check if we collected enough wood
        if(sum >= m)
            ans = i; // possible height, store it
        else
            break; // once wood < m, further heights will also give less
    
    }
;
    return ans;
}
int main(){
    vector<int>arr {4,42,40,26,46};
    int ans = solution(arr,20);
    cout<<ans<<endl;
    return 0;
}