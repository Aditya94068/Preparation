#include <iostream>
using namespace std;

char grade(int marks)
{
    // if(marks>=90){
    //     return 'A';
    // }
    // else if(marks>=80){
    //     return 'B';
    // }
    // else if(marks>=70){
    //     return 'C';
    // }
    // else{
    //     return 'D';
    // }

    // switch (marks/10)
    // {
    // case 10:
    //     return 'A';
    //     break;
    // case 9:
    //     return 'A';
    //     break;
    // case 8:
    //     return 'B';
    //     break;
    // case 7:
    //     return 'C';
    //     break;
    // case 6:
    //     return 'D';
    //     break;
    // default:
    //     return 'E';
    // }
}
int getSum(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}

int  evenSum(int n){
    int sum =0;
    for(int i = 2;i<=n;i+=2){
        sum = sum + i;
    }
    return sum;
}

void AreaOfCircle(float r){
    float pi = 3.14;
    float Area = 3.14 * r * r;
    cout<<Area;
}


void CheckGivenNumberIsEvenOrOdd(int num ){
    if(num % 2 ==0){
        cout<<"Number is even";
    }
    else{
        cout<<"Number is odd";
    }
}

int factorial(int n){
    int fac = 1;
    if(n == 0){
        return 0;
    }
    for (int i=n;i>=1;i--){
        fac = fac * i;
    }
    return fac;
}


// bool  isprime(int n){
//     for (int i=2;i<n;i++){
//         if(n % i ==0){
//             return false;
//         }
        
//     }
//     return true;
// }



bool PrintPrime(int n){
    for(int i = 2;i<n;i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}


int Max(int a , int b , int c){
    if(a > b && a>c){
        return a;
    }
    else if(b>a && b>c){
        return b;
    }
    else{
        return c;
    }
    
}

int main()
{
    // int marks;
    // cin >> marks;
    // cout << grade(marks);
    // for(int i=0;i<=100;i++){
    //     cout<<"Grade of the student : "<<i<<" "<<grade(i)<<endl;
    // }
    // int n;
    // cin>>n;
    // int ans = getSum(n);
    // cout<<"SUM Upto :"<<ans<<endl;

    int a , b , c;
    cin>>a>>b>>c;
    cout<<Max(a , b , c );




    // int n;
    // cout<<"Enter a number :";
    // cin>>n;
    // int ans = evenSum(n);
    // cout<<ans;

    // float r;
    // cout<<"Enter a radius : ";
    // cin>>r;
    // AreaOfCircle(r);

    // int n;
    // cin>>n;
    // CheckGivenNumberIsEvenOrOdd(n);

    // int n;
    // cin>>n;
    // int ans = factorial(n);
    // cout<<ans;

    // int n;
    // cin>>n;
    // if(isprime(n) == false){
    //     cout<<"Number is Not prime ";
    // }
    // else{
    //     cout<<"Number is prime";
    // }



    // int n;
    // cout<<"Enter a number :";
    // cin>>n;
    // for(int i = 2;i<=n;i++){
    //     bool isPrime = PrintPrime(i);
    //     if(isPrime){
    //         cout<<i<<" ";
    //     }
    // }
    
    return 0;
}