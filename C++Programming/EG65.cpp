#include<iostream>
using namespace std;
class Math{
    public:
    int sum(int a, int b)
    {
        return a + b;
    }
    int sum(int a , int b , int c)
    {
        return a + b + c;
    }
    int sum(int a , float b)
    {
        return a + b + 10;
    }
};
int main()
{   
    Math m;
    cout<<m.sum(1,2)<<endl;
    cout<<m.sum(3,4,6)<<endl;
    cout<<m.sum(5,6.4f)<<endl;
    return 0;
}