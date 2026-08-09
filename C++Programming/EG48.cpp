#include<iostream>
#include<algorithm>
using namespace std;
void reverseString(string& str,int start , int end)
{
    if(start >= end){
        return;
    }
    swap(str[start],str[end]);
    reverseString(str,start + 1,end -1);
}
int main()
{
    string str = "abcde";
    int n = str.size();
    int i = 0;
    reverseString(str,i,n-1);
    cout<<str<<endl;
    return 0;
}