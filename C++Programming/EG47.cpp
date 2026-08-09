#include<iostream>
using namespace std;
void lastOccLR(string &s,char &x,int i, int &ans)
{
    //base case
    if(i>=s.size())
      {
        return;
    }
    //ek case solution
    if(s[i] == x){
        ans = i;
    }  
    lastOccLR(s,x,i+1,ans);
}
void lastOccRL(string &s , char &x ,int i,int & ans)
{
    if(i<0)
    {
        return ;
    }
    if(s[i] == x)
    {
        ans = i;
        return;
    }
     lastOccRL(s,x,i-1,ans);
}
int main()
{
    string s;
    cin>>s;
    char x;
    cin>>x;
    int ans = -1;
    // lastOccLR(s,x,0,ans);
    // cout<<ans<<endl;
    lastOccRL(s,x,s.size()-1,ans);
    cout<<ans<<endl;
    return 0;
}