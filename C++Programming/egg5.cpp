#include<iostream>
using namespace std;
int main()
{
    string s = "ABC";
    s = "ABA";
    s[1] = 'c';
    cout<<s<<endl; 
    return 0;
}