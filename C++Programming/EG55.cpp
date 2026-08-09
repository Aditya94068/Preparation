#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<int,char>mpp;
    string s = "tree";
    int freq[26] = {0};
    for(int i = 0;i<s.size();i++)
    {
        mpp[s[i]]++;
        freq[s[i] - 'a']++;
    }
    for(auto it : mpp)
    {
        cout<<it.first<<" "<<it.second<<endl;
    }
    for(int i = 0;i<26;i++)
    {
        cout<<freq[i]<<" ";
    }

    // string s = "abc";
    // for(int i = 0;i<26;i++)
    // {
    //     mpp[i + 1] = 'z' -  i;
    // }
    // // for(auto it : mpp)
    // // {
    // //     cout<<it.first<<" "<<it.second<<endl;
    // // }
    // vector<int>ans;
    // for(auto ch : s)
    // {
    //     mpp[] 
    // }
    // for(int i = 0;i<ans.size();i++){
    //     cout<<ans[i]<<" ";
    // }
    return 0;
}