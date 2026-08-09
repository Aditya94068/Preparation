#include<iostream>
#include<string.h>
using namespace std;
int main(){
    // char ch[] = {'B','\0','A','B','B','\0','A','R'};
    // string str = "ba\0bba\0r";
    // cout<<ch<<endl;
    // cout<<str<<endl;

    string sentence = "hello jee kaise ho saare " ;
    string target = "kaise";
    if(sentence.find(target) == string ::npos){
        cout<<"Not found"<<endl;
    }
    else{
        cout<<"found"<<endl;
    }
    return 0;
}