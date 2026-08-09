#include<iostream>
#include<vector>
using namespace std;
void PrintWaveMatrix(vector<vector<int>>&arr){
    int m = arr.size();
    int n = arr[0].size();

    cout<<"COLUMN WISE WAVE PRINT"<<endl;
    int startCol ;
    // for(startCol = 0;startCol<n;startCol++){
    //     if((startCol & 1) == 0){
    //         for(int i =0;i<m;i++){
    //             cout<<arr[i][startCol]<<" ";
    //         }
    //     }
    //     else {
    //         for(int i = m-1;i>=0;i--){
    //             cout<<arr[i][startCol]<<" ";
    //         }
    //     }
    // }
  
    // for(int startcol = 0;startcol<n;startcol++){
    //     if((startcol & 1) ==0){
    //         for(int i =0;i<m;i++){
    //             cout<<arr[i][startcol]<<" ";
    //         }
    //     }
    //     else 
    //     {   for(int i  = m-1;i>=0;i--){

    //         cout<<arr[i][startcol]<<" ";
    //     }
    //     }
    // }
    cout<<endl;
    cout<<"ROW WISE WAVE PRINT"<<endl;
    int startRow;
    // for(int startRow = 0 ;startRow<m;startRow++){
    //     if((startRow & 1) ==0){
    //         for(int j = 0;j<n;j++){
    //             cout<<arr[startRow][j]<<" ";
    //         }
    //     }
    //     else {
    //         for(int j = n-1;j>=0;j--){
    //             cout<<arr[startRow][j]<<" ";
    //         }
    //     }
    // }

    for(startRow = 0;startRow<n;startRow++){
        if((startRow &1)==0){
            for(int j =0;j<n;j++){
                cout<<arr[startRow][j]<<" ";
            }
        }
        else{
            for(int j =n-1;j>=0;j--){
                cout<<arr[startRow][j]<<" ";
            }
        }
    }
}
int main()
{
    vector<vector<int>>arr {{1,2,3,4},
                            {5,6,7,8},
                            {9,10,11,12}};
    PrintWaveMatrix(arr);
    return 0;
}