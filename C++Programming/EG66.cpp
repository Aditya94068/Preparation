#include<iostream>
using namespace std;
class Param{
    public:
    int val;
    void operator+(Param &obj)
    {
        int value1 = this->val;
        int value2 = obj.val;
        cout<<value2 - value1<<endl;
    }
};
int main()
{   
    Param object1,object2;
    object1.val = 7;
    object2.val = 2;
    object1 + object2;
    return 0;
}