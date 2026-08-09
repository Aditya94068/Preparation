#include<bits/stdc++.h>
using namespace std;
int main()
{
    // vector<string>names {"Mary","John","Emma"};
    // vector<int> heights {180,165,170};
    //   map<int,string>mpp;
    //     for(int i = 0;i<heights.size();i++)
    //     {
    // //         mpp[heights[i]] = names[i];
    // //     }
    // // for(auto val : mpp)
    // // {
    // //     cout<<val.second << " "<<val.first<<endl;
    // // }
    // // vector<string>str{};
    // // for(auto val : mpp)
    // // {
    // //     str.push_back(val.second);
    // // }
    // // reverse(str.begin(),str.end());


    // vector<string>arr = {"d","b","c","b","c","a","e"};
    // int k = 2;
    // map<string,int>mpp;
    //     for(auto it : arr)
    //     {
    //         mpp[it]++;
    //     }
    //     vector<string>ans;
    //     for(auto it : mpp)
    //     {
    //         if(it.second == 1)
    //         {
    //             ans.push_back(it.first);
    //         }
    //     }
    // for(auto it : mpp)
    // {
    //     cout<<it.first<<" "<<it.second<<endl;
    // }
    // for(int i = 0;i<ans.size();i++)
    // {
    //     cout<<ans[i]<<" "<<endl;
    // }
    
    
    
    
    
    
    int n = 2;
    int m = n;
    vector<vector<int>>arr(n,vector<int>(m));
    int num = 0;
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
           arr[i][j] = num;
           num++;
        }
    }
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
    int i = 0;
    int j = 0;
    vector<string> command = {"RIGHT","DEOWN"};
    for(string c : command)
    {
        if(c == "RIGHT")j++;
        else if(c == "DOWN")i++;
        else if(c == "TOP") i--;
        else if(c == "LEFT") j--;
    }
    cout<<arr[i][j]<<" ";
    return 0;


}