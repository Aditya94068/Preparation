// #include<iostream>
// #include<algorithm>
// #include<vector>
// using namespace std;
// int oddOccuring(vector<int>arr){
//     int start =0;
//     int end = arr.size()-1;
//     int mid = start + (end -start)/2;
//     while(start <=end){
//        if(start == end){
//         return start;
//        }
//        if(mid % 2  ==0){
//         if(arr[mid]==arr[mid + 1]){
//             start = mid + 2;
//         }
//         else {
//             end = mid;
//         }
//        }
//        else{
//         if(arr[mid] ==arr[mid-1])
//         {
//             start = mid + 1;
//         }
//         else{
//             end = mid -1 ;
//         }
//        }
//         mid = start + (end -start)/2;
//     }
//     return -1;
// }
// int findPivot(vector<int>arr)
// {
//     int start = 0;
//     int end = arr.size();
//     int mid = start + (end - start)/2;
//     while(start<=end){
//         if(start == end){
//             return start;
//         }
//         if(arr[mid] > arr[mid + 1] && mid + 1 <=end){
//             return mid ;
//         }
//         if(arr[mid] < arr[mid - 1] && mid - 1>=start){
//             return mid - 1;
//         }
//         if(arr[mid] < arr[start]){
//             end = mid - 1;
//         }
//         else{
//             start = mid + 1;
//         }
//         mid = start + (end - start)/2;
//     }
//     return -1;
// }
// int main(){
//      vector<int>arr ={1,1,2,2,3,3,4,4,3,100,100,600,600,4,4};
//     int ans = oddOccuring(arr);
//     cout<<"Index = "<<ans<<endl;
//     cout<<"Element = "<<arr[ans]<<endl;
//     vector<int>nums {9,10,11,12,13,2,3,4,5,6,7,8};
//     int result = findPivot(nums);
//     cout<<result<<endl;
//     cout<<nums[result]<<endl;
//     return 0;
// }

