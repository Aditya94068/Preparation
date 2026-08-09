#include<iostream>
#include<vector>
using namespace std;
// bool BinarySearch(int arr[][4],int row,int col,int target){
//     int totalelement = row * col;
//     int start =0;
//     int end = totalelement - 1;
//     int mid = start  + (end  - start)/2;
//     while(start<=end){
//         int rowIndex = mid/col;
//         int colIndex = mid % col;
//         int element = arr[rowIndex][colIndex];
//         if(element == target){
//             cout<<"Index:"<<rowIndex<<" "<<colIndex<<endl;
//             return true;
//         }
//         else if(element > target){
//             end = mid -1;
//         }
//         else if(element < target){
//             start = mid +1;
//         }
//         mid = start + (end - start)/2;
//     }
//     return false;
// }
bool BinarySearch(int arr[][4],int row ,int col ,int target){
    int start = 0;
    int totalElemtent = row * col;
    int end = totalElemtent -1;
    int mid = start + (end - start)/2;
    while(start<=end){
        int rowIndex = mid /col;
        int colIndex = mid % col;
        int element = arr[rowIndex][colIndex];
        if(element == target){
            cout<<"("<<rowIndex<<","<<colIndex<<")"<<endl;
            return true;
        }
        else if(element>target){
            end = mid -1;
        }
        else if(element<target){
            start = mid + 1;
        }
        mid = start + (end - start)/2;
    }
    return false;
}
int main(){
    int arr[5][4] = {{1,2,3,4},
                     {5,6,7,8},
                     {9,10,11,12},
                     {13,14,15,16},
                     {17,18,19,20}};
    if(BinarySearch(arr,5,4,18 )){
        cout<<"FOUND"<<endl;
    }
    else {
        cout<<"NOT FOUND"<<endl;
    }
    return 0;
}