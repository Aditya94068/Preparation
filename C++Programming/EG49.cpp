#include<iostream>
#include<string>
using namespace std;
bool palindrome_check(string& str,int start ,int end)
{
    if(start >= end)
    {
        return true;
    }
    if(str[start] != str[end])
    {
        return false;
    }
    return palindrome_check(str,start+1,end-1);
}
int main()
{
    string str = "madaam";
    int n = str.size();
    int i = 0;
    bool isPalindrome= palindrome_check(str,i,n-1);
    if(isPalindrome)
    {
        cout<<"Palindrome"<<endl;
    }
    else{
        cout<<"Not a palindrome"<<endl;
    }
    return 0;
}