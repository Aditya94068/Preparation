#include<iostream>
#include<math.h>
#include<climits>
#include<typeinfo>
using namespace std;
int rotation(int arr[]){
     int mini = INT_MAX;
    int index = 6;
    for(int i=0;i<5;i++){
        if(arr[i] < mini){
            mini = arr[i];
            index = i;
        }
    }
   return index;

}
int main(){
    int arr[] = {1,2};
    int ans = rotation(arr);
    cout<<ans<<endl;
    return 0;
}