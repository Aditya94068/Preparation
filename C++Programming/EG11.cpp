#include<iostream>
#include<vector>
using namespace std;
void findMissingElement(vector<int>arr)
{
    // for(int i =0;i<arr.size();i++){
    //     int index = abs(arr[i]);
    //     if(arr[index-1]>0){
    //         arr[index-1] *=-1;
    //     }
    // }
    // for(int i =0;i<arr.size();i++){
    //     if(arr[i]>0){
    //         cout<<i+1<<" ";
    //     }
    // }


    // for (int i = 0;i<arr.size();i++){
    //     int index = arr[i];
    //     if(arr[index-1] >0){
    //         arr[index-1] *=-1;
    //     }
    // }
    // for(int i = 0;i<arr.size();i++){
    //     if(arr[i]>0){
    //         cout<<i+1<<" ";
    //     }
    // }


    // int i =0;
    // while(i<arr.size()){
    //     int index = arr[i];
    //     if(arr[i]!=arr[index-1])
    //     {
    //         swap(arr[i],arr[index-1]);
    //     }
    //     else{
    //         i++;
    //     }
    // }
    // for(int i =0;i<arr.size();i++){
    //     if(arr[i] !=i+1)
    //     {
    //         cout<<i+1<<" ";
    //     }
    // }

   int i =0;
   while(i<arr.size()){
        int index = arr[i];
        if(arr[index-1]!=arr[i]){
            swap(arr[index-1] ,arr[i]);
        }
        else{
            i++;
        }
    }
    for(int i =0;i<arr.size();i++){
        if(arr[i] !=i+1){
            cout<<i+1<<" ";
        }
    }

}
int main(){
    vector<int>arr {1,3,4,3,5};
    findMissingElement(arr);
    return 0;
}