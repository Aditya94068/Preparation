#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<string>str ={"011001","000000","010100","001000"};

    vector<int>ans ;
    int count1 = 0;
    for(int i = 0;i<str.size();i++)
    {
        int count = 0;
        
        for(int j = 0;j<str[i].size();j++)
        {
            if(str[i][j] == '1')
            {
                count++;
            }            
        }
        count1 = count;
        ans.push_back(count1);
    }
    int mul;
    for(int i = 0;i<ans.size();i++)
    {
        mul = ans[i];
        if(count1 != 0)
        {
            mul = mul * count1;
        }
    }
    return 0;
}