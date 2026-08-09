#include<iostream>
#include<cmath>
using namespace std;
// int dicmaltobinaryMethod1(int n){
//     int binary_no = 0;
//     int i = 0;
//     int place = 1;
//     while(n>0){
//         int bit = n % 2;
//         binary_no = bit*place + binary_no;
//         place *= 10;
//         n = n/2;
//     }
//     return binary_no;
// }


int dicmaltobinaryMethod2(int n){
    int binary_no = 0;
    int i = 0;
    int place = 1;
    while(n>0){
        int bit = (n & 1);
        binary_no = bit*place + binary_no;
        place *=10;
        n = n>>1;
    }
    return binary_no;
}

int binarytodecimal(int n){
    int decimal = 0;
    int i = 0;
    while (n){
        int bit = n % 10;
        decimal = bit * pow(2,i++) + decimal;
        n = n/10;
    }

    return decimal;
}
int main(){
    // int n;
    // cin>>n;
    // int binary = dicmaltobinaryMethod1(n);
    // cout <<binary;


    // int binary = dicmaltobinaryMethod2(n);
    // cout <<binary;

    int binaryno;
    cin>>binaryno;
    int ans = binarytodecimal(binaryno);
    cout<<ans;

    return 0;
}