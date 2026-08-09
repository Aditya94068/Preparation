#include<iostream>
#include<vector>
using namespace std;
void printSubsequences(string str,vector<string>&ans,int i ,string output)
{
    if(i>=str.length())
    {
        ans.push_back(output);
        return;
    }
    printSubsequences(str,ans,i+1,output);
    output = output + str[i];
    printSubsequences(str,ans,i+1,output);
}

int main()
{   
    string str = "abc";
    string output = "";
    vector<string> ans;
    int i = 0;
    printSubsequences(str,ans,i,output);
    for(int i = 0;i<ans.size();i++)
    {
        cout<<ans[i]<<endl;
    }
}