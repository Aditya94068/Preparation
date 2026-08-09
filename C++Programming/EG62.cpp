#include<iostream>
using namespace std;
class Aditya_Vaishnav{
    public:
    string name;
    string gender;
    string college;
    int age;
    long long prn;
    Aditya_Vaishnav(string name, string gender,string college,long long prn,int age)
    {
        this->name = name;
        this->gender = gender;
        this->college = college;
        this->prn = prn;
        this->age  = age;
        cout<<"Name :"<<name<<endl;
        cout<<"Gender :"<<gender<<endl;
        cout<<"college:"<<college<<endl;
        cout<<"PRN :"<<prn<<endl;
        cout<<"Age :"<<age<<endl;
    }
    Aditya_Vaishnav(Aditya_Vaishnav &obj){
        cout<<"Copy Constructor"<<endl;
        this->name = obj.name;
        this->gender = obj.gender;
        this->college =obj.college;
        this->prn = obj.prn;
        this->age  = obj.age;
        cout<<"Name :"<<name<<endl;
        cout<<"Gender :"<<gender<<endl;
        cout<<"college:"<<college<<endl;
        cout<<"PRN :"<<prn<<endl;
        cout<<"Age :"<<age<<endl;
    }
    ~Aditya_Vaishnav(){
        cout<<"I am Creating the destructor"<<endl;
    }
};
int main()
{
    Aditya_Vaishnav a1("Aditya vaishnav ", "Male","Sandip university ",230105131282,21);
    Aditya_Vaishnav b1 = a1;

    Aditya_Vaishnav* c1 = new Aditya_Vaishnav("Sumit Vaishnav ","Male", "xyz",21324535646,24);
    Aditya_Vaishnav* d1 = new Aditya_Vaishnav(*c1);
    delete d1;
    delete c1;
    return 0;
}