#if !defined(BIRD_H)
#define BIRD_H
#include<iostream>
using namespace std;
class Bird
{
    public:
    virtual void eat() = 0;
    virtual void fly() = 0;
};
class sparrow : public Bird{
    public:
    void eat()
    {
        cout<<"Sparrow is eating"<<endl;
    }  
    void fly()
    {
        cout<<"Sparrow is flying"<<endl;
    }
};
#endif