#include<iostream>
#include<math.h>
using namespace std;
int count = 0;
void printpermutation(string&str,int i)
{
    if(i>=str.length())
    {
        cout<<str<<" ";
        return;
    }
    for(int j = i;j<str.length();j++)
    {
        // cout<<"Inside the loop (1) : "<<str<<endl;
        count++;
        swap(str[i],str[j]);
        printpermutation(str,i + 1);
        
        swap(str[i],str[j]);
        
    }   
}
int main()
{
    string str = "abc";
    int i = 0;
    // printpermutation(str,i);
    bool a = 0;
    cout<<ceil(a)<<endl;
    return 0;
}