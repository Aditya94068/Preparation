#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
int firstRepeatingElement(int arr[]){
    // for(int i =0;i<arr.size();i++){
    //     bool isRepeat = false;
    //     for(int j =i+1;j<arr.size();j++){
    //         if(arr[i] == arr[j])
    //         {
    //             isRepeat = true;
    //             return i+1;
    //         }
    //     }
    // }

    
    // int hash[9]={0};
    // for(int i =0;i<9;i++){
    //     hash[arr[i]]++;
    // }

    // for(int i =0;i<9;i++){
    //     if(hash[arr[i]]>1)
    //     {
    //         return i+1;
    //     }
    // }
    // return -1;  

    int n = 9;
    unordered_map<int,int>Hash;
    for(int i =0;i<n;i++){
        Hash[arr[i]]++;
    }
    for(int i =0;i<n;i++){
        if(Hash[arr[i]]>1){
            return i+1;
        }
    }
    return -1;
}
int main(){
    int arr[] = {1,2,42,90,10,4,90,5,6};
    int n = 9;
    int result = firstRepeatingElement(arr);
    cout<<result<<endl;
    return 0;
}