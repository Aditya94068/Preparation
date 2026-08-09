#include<iostream>
using namespace std;
int dividetwo(int divident , int divisor){
    int start =0;
    int end = abs(divident);
    int mid = start + (end - start)/2;
    int ans = -1;
    while(start<=end){
        if(abs(mid * divisor) == abs(divident))
        {
            ans = mid;
            break;
        }
        if(abs(mid * divisor)> abs(divident)){
           end = mid  -1;
        }
        if(abs(mid * divisor) < abs(divident)){
            ans = mid;
            start = mid + 1;
        }
        mid = start + (end -start)/2;
    }
    if((divident<0  && divisor<0) || (divident>0 && divisor>0))
    {
        return ans;
    }
    else {
        return -ans;
    }
}
int main(){
    int divident = 10;
    int divisor = 3;
    int ans = dividetwo(divident,divisor);
    cout<<ans<<endl;


    int precision ;
    cout<<"Enter a decimal digits :";
    cin>>precision;


    double step = 0.1;
    double finalAns = ans;
    for(int i = 0;i<precision;i++){
        for(double j = finalAns; j * divisor <=divident ; j = j + step){
            finalAns  = j;
        }
        step = step / 10;
    }

    cout<<"Final Ans : "<<finalAns<<endl;
    return 0;
}