#include<iostream>
using namespace std;
class A{
    public:
    int chemistry;
    A(){
        chemistry = 101;
    }
};
class B{
    public:
    int physics;
    int chemistry;
    B(){
        chemistry = 230;
    }
};
class C : public A ,public B{
    public:
    int maths;
};
int main()
{
    C obj;
    //Confusion dur karne ke liye hum scoope resolution operator ka use karte hai 
    cout<<obj.A::chemistry<<" "<<obj.B::chemistry<<" "<<obj.physics<<" "<<obj.maths<<endl;

    return 0;
}