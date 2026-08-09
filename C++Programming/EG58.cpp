#include <iostream>
#include <vector>
#include<bits/stdc++.h>
#include<EG55.cpp>
using namespace std;
int main()
{
    
    // // [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
    // vector<vector<int>> grid{
    //      {1, 2, 3, 4},
    //      {5, 6, 7, 8}, 
    //      {9, 10, 11, 12}, 
    //      {13, 14, 15, 16}};
    // int x = 1;
    // int y = 0;
    // int k = 3;
    // int n = grid.size();
    // int m = grid[0].size();
    // vector<vector<int>> mat(n-x);
    // for (int i = x; i < n; i++)
    // {
    //     for (int j = y; j < k; j++)
    //     {
    //         mat[i - x].push_back(grid[i][j]);
    //     }
    // }
    // for(int i = 0;i<mat.size()/2;i++)
    //     {
    //         swap(mat[i],mat[mat.size() - i -1]);
    //     }
    // for(int i = 0;i<mat.size();i++)
    // {
    //     for(int j = 0;j<mat[0].size();j++)
    //     {
    //         cout<<mat[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    string s = "aaabbccc";
    map<char,int>m;
    for(auto ch : s){
        m[ch]++;
    }
    for(auto it : m)
    {
        cout<<it.first<<"->"<<it.second<<" ";
    }
    
    return 0;
}
