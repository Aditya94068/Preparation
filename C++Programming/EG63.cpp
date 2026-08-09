#include<iostream>
using namespace std;
class Animal{
    private:
    int age;
    int weight;
    public:
    void eat()
    {
        cout<<"I am eating "<<endl;
    }
    int getter()
    {
        return this->age;
    }
    void setter(int age)
    {
        this->age = age;
    }
};
int main()
{
    Animal a1;
    a1.setter(35);
    cout<<a1.getter()<<endl ;
    cout<<"AADITYA VAISHNAV"<<endl;
    return 0;
}