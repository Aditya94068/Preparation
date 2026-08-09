#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
        string s = "Madas";
      int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            char left = s[i];
            char right = s[j];

            if (!isalnum(left)) {
                i++;
                continue;
            }

            if (!isalnum(right)) {
                j--;
                continue;
            }

            if (tolower(left) != tolower(right)) {
                cout<<true<<endl;
            }

            i++;
            j--;
        }
        cout<<"Aditya"<<endl;
        cout<<s.length()-1<<endl;

        char ch1 = 'A';
    char ch2 = 'z';
    char ch3 = '7';

    cout << ch1 << " -> " << (char)tolower(ch1) << endl;
    cout << ch2 << " -> " << (char)tolower(ch2) << endl;
    cout << ch3 << " -> " << (char)tolower(ch3) << endl;

    return 0;
}