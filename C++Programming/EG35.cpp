#include<iostream>
using namespace std;
// void solve(int arr[])
// {
//     cout<<"Size of inside the solve function "<<sizeof(arr)<<endl;
//     cout<<"arr: "<<arr<<endl;
//     cout<<"&arr:"<<&arr<<endl;
//     arr[0] = 50;
// }
void update(int *p){
    *p = *p + 10;
    cout<<"Value in ptr :"<<p<<endl;
    cout<<"Address of ptr is :"<<&p<<endl;
}
int main(){
    // int arr[4] = {12,23,34,54};
    // cout<<arr[0]<<endl;
    // cout<<arr<<endl;
    // cout<<&arr<<endl;
    // cout<<&arr[0]<<endl;

    // int* p = arr;
    // cout<<p<<endl;
    // cout<<&p<<endl;

    // cout<<*arr<<endl;
    // cout<<*arr + 1<<endl;
    // cout<<*(arr) + 1<<endl;
    // cout<<*(arr + 1)<<endl;

    // int i = 0;
    // cout<<arr[i]<<endl;
    // cout<<i[arr]<<endl;
    // cout<<*(arr + i)<<endl;
    // cout<<*(i + arr)<<endl;

    // int* p = arr;
    // cout<<"D"<<*p<<endl;
    // p = p + 2;
    // cout<<*p<<endl;


    // char ch[10] = "Aditya";
    // char* c = ch;

    // cout<<ch<<endl;
    // cout<<&ch<<endl;
    // cout<<ch[0]<<endl;
    
    // cout<<&c<<endl;
    // cout<<*c<<endl;
    // cout<<c<<endl; 

    // char ch = 'k';
    // char* cptr = &ch;
    // cout<<cptr<<endl;

    // int arr[10] = {1,2,3,4};
    // cout<<"Size inside main funcition :"<<sizeof(arr)<<endl;
    // cout<<arr<<endl;
    // cout<<&arr<<endl;
    // // printing array inside main
    // for(int i = 0;i<10;i++){
    //     cout<<arr[i]<<" ";
    // }
    // cout<<endl;
    // cout<<endl<<endl<<"Now calling solve function"<<endl;
    // solve(arr);
    // cout<<"Wapas main function ne aagye h "<<endl;
    // for(int i =0;i<10;i++){
    //     cout<<arr[i]<<" ";
    // }cout<<endl;

    int a = 5;
    cout<<"Value in a : "<<a<<endl;
    cout<<"Address of a is :"<<&a<<endl;
    int *ptr = &a;
    cout<<"Value in ptr : "<<ptr<<endl;
    cout<<"Address of ptr is :"<<&ptr<<endl;
    update(ptr);
    cout<<a<<endl;
    return 0;
}