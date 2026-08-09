#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>arr {1 ,2,-3,-5,4};
   
    int i =0;
    int j ;
    for(j = i+1;j<arr.size();j++)
    {
        if(arr[j]<0)
        {
            swap(arr[i],arr[j]);
            i++;
        }
       
    }
    for(int i = 0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}