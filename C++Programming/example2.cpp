#include<iostream>
#include<vector>
using namespace std;
int main(){
    // string str = "babad";
    // vector<string>Substring;
    // for (int i = 0;i<str.size();i++){
    //     for (int j = i + 1;j<=str.size();j++){
    //         Substring.push_back(str.substr(i,j));
    //     }
    // }
    // for(auto str : Substring){
    //     cout<<str<<" ";
    // }
    string s1 = "aditya";
    string s2 = "vaishnav";
    int n = s1.size();
    int m = s2.size();
    cout<<n - m<<endl;
    cout<<s2[2]<<endl;
    cout<<s1.size()<<endl;

    cout<<s2.length()<<endl;

    return 0;
}