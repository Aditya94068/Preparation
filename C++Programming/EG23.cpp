#include<iostream>
#include<vector>
using namespace std;
int Root(int n){
    int start = 0;
    int end = n;
    int mid = start + (end - start)/2;
    int target = n;
    int ans = -1;
    while(start<=end)
    {
        if(mid * mid == target){
            return mid;
        }
        else if(mid * mid >target){
            end = mid -1;
        }
        else if(mid * mid < target){
            ans = mid;
            start = mid + 1;
        }   

        mid = start + (end - start)/2;
    }
    return ans;
}
int main(){ 
    int n ;
    cout<<"Enter a number "<<":"<<endl;
    cin>>n;
    int ans = Root(n);
    cout<<ans<<endl;

    int precision;
    cout<<"Enter the number of floating digits in presision "<<endl;
    cin>>precision;

    double step = 0.1;
    double finalans = ans;
    for(int i =0;i<precision;i++){
        for(double  j = finalans ; j*j<=n ; j = j + step){
            finalans = j;
        }
        step = step/10;
    }
    cout<<"Final ans is . "<<finalans<<endl;
    return 0;
}