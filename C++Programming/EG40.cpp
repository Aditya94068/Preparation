#include<iostream>
#include<vector>
using namespace std;
int main(){
    string s = "abc";
    vector<string>ans;
    for(int i = 0;i<s.length();i++){
        for(int j = i;j<s.length();j++){
            cout<<s.substr(i,j-i+1)<<" ";
        }
        cout<<endl;
    }
    return 0;
}