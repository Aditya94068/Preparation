#include<iostream>
using namespace std;
class Animal{
    private:
    int weight;
    public:
    int age;  
    string name;
    // Default constructor
    Animal(){
        cout<<"Default constructor called"<<endl;
    }
    // Single  Constructor
    Animal(int age){
        this ->age;
        cout<<"Parameterized constructor called 1 "<<endl;
    }
    Animal(int age , int weight){
        this->age = age;
        this->weight=weight;
        cout<<"Parameterized constructor called 2"<<endl;
    }
    Animal(int age , int weight,string name)
    {
        this->age = age;
        this -> weight = weight;
        this -> name = name;
        cout<<"Parametrized constructor called 3 "<<endl;
    }
    // Copy constructor
    Animal(Animal &obj)
    {
        this-> age = age;
        this ->weight = weight;
        this ->name = name;
        cout<<"I am inside the copy constructor "<<endl;
    }

    ~Animal()
    {
        cout<<"I am inside the destructor "<<endl;
    }
};
int main()
{
    // Object Creation
    // Default Constructor
    Animal a;  
    // Parametrised Constructor
    Animal b(23);
    Animal c(23,53);
    Animal d(23,54,"Aditya");
    // Defau/lt Constructor using new keyword
    Animal* p = new Animal;
    // Parametrised Constructor using new keyword
    Animal * q = new Animal(23);
    Animal* x = new Animal(13,35);
    Animal* y = new Animal(23, 34,"Aditya");
    // Copy Constructor 
    
    Animal s = a;
    Animal animal1 = s;
    //Copy Constructor using pointer because new keyword address return karta hai
    Animal animal2(*p);

    //Destructor is calling using stack memeory 
    Animal animal3;

    // Destructor is calling using heap memory
    Animal* animal4= new Animal();
    delete animal4;
    return 0;
}