#include<iostream>
#include<vector>
using namespace std;
int main(){
    // bool a =  true;
    // bool b = true;
    //  cout<<(~a);
    //  cout<<(a^b);
    // cout<<(2 & 3)<<endl;
    // cout<<(5 & 10)<<endl;
    // cout<<(2 | 5)<<endl;

    // int a = -17;
    // a = a>>1;
    // a = 12<<5;
    // cout<<a;
    // cout<<~(~a)<<endl;

    // int a = 11;
    // cout<<a<<endl;
    // cout<<++a<<endl;
    // cout<<a++<<endl;
    // cout<<a<<endl;

    // int a = 6;
    // int c = ++a + 1;
    // cout<<c;


    // int a = 6;
    // int c = a++ + 1;
    // cout<<c;

    // int a = 3;
    // int b = 4;
    // int c = (++a) * (--b);
    // cout<<c;

    // int a = 5;
    // cout<<(++a) * (++a);

    vector<int>arr = {1,8,9,10,11,12,13,14,15,6,2,3,4,5,7};
    int i  = 0;
    while(i<arr.size()){
        int index = arr[i];
        if(arr[index - 1] !=arr[i]){
            swap(arr[index - 1],arr[i]);
        }
        else i++;
    }
    for(int i =0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}