#include<iostream>
#include<string.h>
using namespace std;
int getlength(char ch[]){
    int length = 0;
    int i = 0;
    while (ch[i] != '\0'){
        length++;
        i++;
    }
    return length;
}
void reverseArray(char arr[]){
     int i = 0;
    //  int n = (arr);
     int j = getlength(arr)-1;
     while(i<=j){
        swap(arr[i],arr[j]);
        i++;
        j--;
     }
}
void replacearr(char sentenced[]){
    int i = 0;
    while(sentenced[i] !='\0')
    {
        if(sentenced[i] == ' '){
            sentenced[i] = '@';
        }
        i++;
    }
}
bool palindrome(char arr[]){
    int i = 0;
    int n = strlen(arr);
    int j = n-1;
    while(i <= j){
        if(arr[i] == arr[j]){
        i++;
        j--;
        }
        else{
            return false;
        }
       
    }
    return true;
}
void convertUpper(char word[])
{
    int i = 0;
    for (int i = 0;i<strlen(word);i++){
        if(word[i] == ' '){
            continue;
        }
        word[i] = word[i] - 32;
    }
}

void convertlower(char word[])
{
    int i = 0;
    for (int i = 0;i<strlen(word);i++){
        if(word[i] == ' '){
            continue;
        }
        if(word[i] >= 'a' && word[i] <= 'z') continue;
        word[i] = word[i] - 'A' + 'a';
        // word[i] = word[i] + 32;
    }
}
int main(){
    // char ch[100] ;
    // cout<<"Enter a name:";
    // cin>>ch;
    // cout<<ch<<endl;

    // char ch[4] = {'l','o','v','e'};
   
    // cout<<ch<<endl;

    // char ch[15];
    // cout<<"Enter a name :"<<endl;
    // cin>>ch;
    // cin.getline(ch,50);
    // cout<<ch<<endl;

    // char ch[50];
    // cin>>ch[49];
    // cin>>ch[2];
    // cin.getline(ch,50);
    // cout<<ch<<endl;

    // char ch[100];
    // cout<<"Enter a ch :";
    // cin.getline(ch,100);
    // int n = getlength(ch);
    // cout<<n<<endl;
    // cout<<strlen(ch)<<endl;
    // cout<<"Before array :"<<ch<<endl;
    // reverseArray(ch);
    // cout<<"After array :"<<ch<<endl;

    char sentenced[100];
    cout<<"Enter a sentenced :";
    cin.getline(sentenced,100);
    // cout<<"Before replace :"<<sentenced<<endl;
    // replacearr(sentenced);
    // cout<<"After replace :"<<sentenced<<endl;

    // cout<<palindrome(sentenced);

    // convertUpper(sentenced);
    // cout<<sentenced<<endl;
    convertlower(sentenced);
    cout<<sentenced<<endl;
    return 0;
}