#include <iostream>
#include <assert.h>
using namespace std;
int main()
{
    // int n;
    // if(cin>>n){
    //     cout<<"Aditya Vaishnav"<<endl;
    // }

    // if(""){
    //     cout<<"vaishnav"<<endl;
    // }
    // string str = "";
    // if(str.empty()){
    //     cout<<"Empty String "<<endl;
    // }
    // if(""){
    //     cout<<"Aditya"<<endl;
    // }

    // int n ;
    // cin>>n;

    // outer loop
    //  for (int row = 0;row<3;row = row + 1){
    //      //Inner loop
    //      for (int col = 0;col<5;col = col + 1){
    //          cout<<"*"<<" ";
    //      }
    //      cout<<endl;
    //  }

    // for (int row = 0;row<n;row +=1){
    //     for (int col = 0;col < n;col +=1){
    //         cout<<"*"<<" ";
    //     }
    //     cout<<endl;
    // }

    // int n,m;
    // cin>>n;
    // cin>>m;
    // for (int row = 0;row < n;row = row + 1){
    //     if(row == 0 || row == n-1){
    //     for (int col = 0;col<m;col = col + 1){
    //         cout<<"*"<<" ";
    //     }
    //    }
    //    else{
    //     cout<<"*"<<" ";
    //     for (int i = 0 ;i<m-2;i++){
    //         cout<<"  ";
    //     }
    //     cout<<"* ";
    //    }
    //    cout<<endl;
    // }

    // int n;
    // cin>>n;
    // for (int row = 0;row <n;row = row + 1){
    //     for (int col = 0;col<row+1;col = col + 1){
    //         cout<<"* ";
    //     }
    //     cout<<endl;
    // }

    // int n;
    // cin>>n;
    // for (int row = 0; row < n;row= row + 1){
    //     for (int col = n - row ; col > 0 ;col = col - 1){
    //         cout<<"* ";
    //     }
    //     cout<<endl;
    // }
    // return 0;

    // int n ;
    // cin>>n;
    // for (int row = 0; row <n;row = row +1){
    //     for (int col = 0 ; col<row+1;col = col + 1){
    //         cout<<col + 1<<" ";
    //     }
    //     cout<<endl;
    // }

    // int n ;
    // cin>>n;
    // for (int row = 0 ;row <n;row = row + 1){
    //     for (int col = 0 ; col <n-row;col = col + 1){
    //         cout<<col + 1<<" ";
    //     }
    //     cout<<endl;
    // }

    //  int n;
    // cin>>n;
    // for (int row = 0 ; row < n ; row = row + 1)
    // {
    //     for (int col = 0 ; col < n-row - 1 ; col++){
    //         cout<<" ";
    //     }
    //     for (int col = 0 ; col <row + 1 ; col++){
    //         cout<<"* " ;
    //     }
    //     cout<<endl;
    // }

    //   int n;
    //   cin>>n;
    //   for(int i= 0 ;i<n;i++){
    //     for (int j = 0 ;j<i;j++){
    //         cout<<" ";
    //     }
    //     for (int j = 0 ;j<n-i;j++){
    //         cout<<"* ";
    //     }
    //     cout<<endl;
    // }

    // int n;
    // cin >> n;
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if (i == 0 || j == 0 || j == n - i - 1)
    //         {
    //             cout << "* ";
    //         }
    //         else
    //         {
    //             cout << "  ";
    //         }
    //     }
    //     cout << endl;
    // }

    //  int n;
    //  cin>>n;
    //  for(int i=0;i<n;i++){
    //     int k = 0;
    //     for (int j = 0 ;j<2*n-1;j++){
    //         if(j<n-i-1){
    //             cout<<" ";
    //         }
    //         else if(k<2*i+1){
    //             if(k==0 || k==2*i || i==n-1){
    //                 cout<<"*";
    //             }
    //             else{
    //                 cout<<" ";
    //             }
    //             k++;
    //         }
    //         else{
    //             cout<<" ";
    //         }
    //     }
    //     cout<<endl;
    //  }

    // int n;
    // cin>>n;
    // for (int row = 0 ; row < n ; row = row + 1)
    // {
    //     for (int col = 0 ; col < n-row - 1 ; col++){
    //         cout<<" ";
    //     }
    //     for (int col = 0 ; col <row + 1 ; col++){
    //         cout<<"* " ;
    //     }
    //     cout<<endl;
    // }
    // for(int i= 0 ;i<n;i++){
    //     for (int j = 0 ;j<i;j++){
    //         cout<<" ";
    //     }
    //     for (int j = 0 ;j<n-i;j++){
    //         cout<<"* ";
    //     }
    //     cout<<endl;
    // }

    // int n;
    // cin>>n;
    // for(int i=0;i<n;i++){
    //     for(int j = 0;j<n-i-1;j++){
    //         cout<<" ";
    //     }
    //     for(int j = 0;j<2*i+1;j++){
    //         if(j==0 || j==2*i)
    //         {
    //             cout<<"*";
    //         }
    //         else{
    //             cout<<" ";
    //         }
    //     }
    //     cout<<endl;
    // }


    // for(int i=0;i<n;i++)
    // {
    //     for(int j=0;j<i;j++){
    //         cout<<" ";
    //     }
    //     for(int j=0;j<2*n-2*i-1;j++){
    //         if(j==0||j==(2*n - 2*i -2))
    //         {
    //             cout<<"*";
    //         }
    //         else{
    //             cout<<" ";
    //         }
    //     }
    //     cout<<endl;
    // }

    // int n;
    // cin>>n;
    // for (int i=0;i<n;i++){
    //     for (int j=0;j<n-i;j++){
    //         cout<<"*";
    //     }
    //      for(int j=0;j<2*i+1;j++){
    //         cout<<" ";
    //     }

    //    for(int j=0;j<n-i;j++){
    //      cout<<"*";
    //    }
    //     cout<<endl;
    // }
    // for(int i=0;i<n;i++){
    //    for(int j=0;j<i+1;j++){
    //        cout<<"*";
    //    }
    //    for(int j=0;j<2*n-2*i-1;j++)
    //     {
    //         cout<<" ";
    //     }
    //     for(int j=0;j<i+1;j++){
    //         cout<<"*";
    //     }
    //     cout<<endl;
    //     }
    

    //  for(int i=0;i<n;i++){
    //     int j;
    //     for(j =0;j<i+1;j++){
    //         int ans = j + 1;
    //         char ch = ans + 'A' - 1;
    //         cout<<ch;
    //     }

    //     for(int j = i;j>=1;j--){
    //         int ans = j;
    //         char ch = ans +'A'-1;
    //         cout<<ch;
    //     }
    //     cout<<endl;
    // }

    // for(int i=0;i<n;i++){
    //    if(i ==0 || i==n-1){
    //         for(int j = 0;j<n;j++){
    //             cout<<"*";
    //         }
    //    }
    //    else{
    //     cout<<"*";
    //     for(int j=0;j<n-2;j++){
    //         cout<<" ";
    //     }
    //     cout<<"*";
    //    }
    //    cout<<endl;
    // }

    // int n;
    //  cin>>n;
    //  for(int i=0;i<n;i++){
    //     int k = 0;
    //     for (int j = 0 ;j<2*n-1;j++){
    //         if(j<n-i-1){
    //             cout<<" ";
    //         }
    //         else if(k<2*i+1){
    //             if(k==0 || k==2*i || i==n-1){
    //                 cout<<"*";
    //             }
    //             else{
    //                 cout<<" ";
    //             }
    //             k++;
    //         }
    //         else{
    //             cout<<" ";
    //         }
    //     }
    //     cout<<endl;
    //  }

    // int n;
    // cin>>n;
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<i+1;j++)
    //     {   if( j==0 | i==n-1||j==i)
    //         {
    //             cout<<j+1<<" ";
    //         }
    //         else{
    //             cout<<"  ";
    //         }
    //     }
    //     cout<<endl;
    // }


    // for(int i=0;i<n;i++){
    //     for(int j=i+1;j<=n;j++)
    //     { 
    //        cout<<j<<" ";     
    //     }
    //     cout<<endl;
    // }

    
    // for(int i=0;i<n;i++){
    //     for(int j=i+1;j<=n;j++)
    //     { 
    //         if(j==i+1 || j==n||i==0){

    //             cout<<"*"<<" ";     
    //         }
    //         else{
    //             cout<<"  ";
    //         }
    //     }
    //     cout<<endl;
    // }

//     int n;
//     cin>>n;
//     int k = n;
//     for(int i =0;i<n;i++){
//         int c = 1;
//         for(int j=0;j<k;j++){
//             if(j<n-i-1){
//                 cout<<" ";
//             }
//             else if(j<=n-1){
//                 cout<<c;
//                 c++;
//             }
//             else if(j==n){
//                 c = c-2;
//                 cout<<c;
//                 c--;
//             }
//             else{
//                 cout<<c;
//                 c--;
//             }
//         }
//         k++;
//         cout<<endl;
//     }






// int n;
// cin>>n;
// for(int i=0;i<2*n-1;i++){
//     int cond=0;
//     if(i<n)
//     {
//         cond = i;
//     }
//     else{
//         cond = n - (i % n) -2;
//     }
//     // int cond = i<n ? i:n-(i%n) - 2;
//     for(int j=0;j<=cond;j++){
//         cout<<"*";
//     }
//     cout<<endl;
// }

// int n;
// cin>>n;
// for(int i=0;i<n;i++){
//     int start_num_index=8-i;
//     int num = i + 1;
//     int count_num = num;
//     for(int j=0;j<17;j++){
//         if(j==start_num_index && count_num>0)
//         {
//             cout<<num;
//             start_num_index +=2;
//             count_num --;
//         }
//         else{
//             cout<<"*";
//         }
//     }
//     cout<<endl;
// }


// int n;
// cin>>n;
// for(int i=0;i<n;i++){
//     for(int j=0;j<n-i-1;j++){
//         cout<<" ";
//     }
//     for(int j=0;j<i+1;j++){
//         cout<<i+j+1;
//     }
//     int start = 2 *i;
//     for(int j=0;j<i;j++){
//         cout<<start;
//         start = start -1;
//     }
//     cout<<endl;
// }



// int n;
// cin>>n;
// for(int i=0;i<n;i++){
//     for(int j=0;j<n-i-1;j++){
//         cout<<" ";
//     }
//     int start = 1;
//     for(int j=0;j<2*i+1;j++){
//         if(i==0 || i==n-1){
//             if(j%2==0)
//             {
//                 cout<<start;
//                 start = start + 1;
//             }
//             else{
//                 cout<<" ";
//             }
//         }
//         else{
//             if(j==0){
//                 cout<<1;
//             }
//             else if(j == 2*i+1-1)
//             {
//                 cout<<i+1;
//             }
//             else{
//                 cout<<" ";
//             }
//         }
//     }
//     cout<<endl;
// }



}