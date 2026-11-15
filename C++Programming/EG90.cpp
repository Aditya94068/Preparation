#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "xyzbbar";
    unordered_map<char,int>mpp;
    for(int i =0;i<s.size();i++)
    {
        mpp[s[i]]++; 
    }
    for(int i = 0;i<s.size();i++)
    {
        if(mpp[s[i]] > 1)
        {
            cout<<s[i]<<"->"<<i<<endl;
            break;
        }
    }
    return 0;
}