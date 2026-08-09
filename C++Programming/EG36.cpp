#include<bits/stdc++.h>
using namespace std;
int main(){
    // int a = 5;
    // int *p = &a;
    // int**q = &p;
    // cout<<**q<<endl;
    // cout<<*q<<endl;
    // cout<<*p<<endl;
    // cout<<&p<<endl;
    // cout<<&q<<endl;
    // cout<<&a<<endl;

    // Reference variable
    int a = 5;
    int& b = a;
    cout<<a<<endl;
    cout<<b<<endl;
    a++;
    cout<<a<<endl;
    cout<<b<<endl;
    b++;
    cout<<a<<endl;
    cout<<b<<endl; 
    return 0;
}