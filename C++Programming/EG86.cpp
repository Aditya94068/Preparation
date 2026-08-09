#include<bits/stdc++.h>
using namespace std;
int fibonaaci(int n)
{
    if(n == 0)
    {
        return 0;
    }
    if(n == 1) return 1;
    return fibonaaci(n-1) + fibonaaci(n - 2);
}

// 1-D dp 
int fibonaaciusingMemo(int n,vector<int>& dp)
{
    if(n == 0)
    {
        return 0;
    }
    if(n == 1) return 1;
    int ans =  fibonaaciusingMemo(n-1,dp) + fibonaaciusingMemo(n - 2,dp);
    dp[n] = ans;
    return dp[n];
}
int main()
{ 
    int n = 5;
    vector<int>dp(n+1,-1);
    int ans = fibonaaciusingMemo(n,dp);

    return 0;
}