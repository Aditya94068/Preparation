#include<iostream>
using namespace std;
int printPowerOfTwo(int i , int n)
{
    if(n==1)
    {
        return 2;
    }
    return 2 * printPowerOfTwo(2,n-1);
}
int main()
{
    int n = 5;
    cout<<printPowerOfTwo(2,n);
    return 0;
}