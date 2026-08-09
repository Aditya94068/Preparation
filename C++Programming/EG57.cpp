#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
     vector<vector<int>> mat = {{0, 0, 0}, {0, 1, 0}, {1, 1, 1}};
    int n = 3;
    int m = 3;
    vector<vector<int>> arr(n, vector<int>(m, 0));
    for(int k = 0;k<=3;k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                arr[i][j] = mat[j][i];
            }
        }
        for (int i = 0; i < n; i++)
        {
            int start = 0;
            int end = m - 1;
            while(start < end)
            {
                swap(arr[i][start],arr[i][end]);
                start++;
                end--;
            }
        }
        cout<<"arr"<<endl;
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<m;j++)
            {
                cout<<arr[i][j]<<" ";
            }
            cout<<endl;
        }
        cout<<"change arr"<<endl;
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<n;j++)
            {
                mat[i][j] = arr[i][j];
            }
        }
    }
        return 0;
}