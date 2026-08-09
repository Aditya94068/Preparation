#include<bits/stdc++.h>
using namespace std;
class TrieNode{
    public:
    char data;
    TrieNode * children[26];
    bool isTerminal;
    TrieNode(char d)
    {
        this->data = d;
        for(int i = 0;i<26;i++)
        {
            children[i] = NULL;
        }
        this -> isTerminal = false;
    }
};
void insertWord(TrieNode* root , string word)
{
    cout<<"Inserting "<<word<<endl;
    if(word.length() == 0)
    {
        root -> isTerminal = true;
        return;
    }
    char ch = word[0];
    int index = ch - 'A';
    TrieNode * child;
    if(root->children[index] != NULL)
    {
        child = root->children[index];
    }
    else{
        child = new TrieNode(ch);
        root->children[index] = child;
    }
    insertWord(child,word.substr(1)); 
}
bool search(TrieNode* root , string word){
    if(word.length() == 0){
        return root->isTerminal;
    }
    char ch = word[0];
    int index = ch - 'A';
    TrieNode * child;
    if(root->children[index] != NULL)
    {
        child = root->children[index];
    }else{
        return false;
    }
    return search(child,word.substr(1));
}
void deleteword(TrieNode* root,string word)
{
    if(word.length() == 0){
        root->isTerminal = false;
        return;
    }
    char ch = word[0];
    int index = ch - 'A';
    TrieNode* child;
    if(root->children[index] != NULL)
    {
        child = root->children[index];  
    }
    else{
        return;
    }
    deleteword(child,word.substr(1));
}
int main(){

    TrieNode* root = new TrieNode('-');
    insertWord(root,"ADITYA");
    if(search(root,"ADITYA")){
        cout<<" presend" <<endl;
    }
    else{
        cout<<"absent"<<endl;
    }
    deleteword(root,"ADITYA");
    if(search(root,"ADI")){
        cout<<" presend" <<endl;
    }
    else{
        cout<<"absent"<<endl;
    }
    return 0;
}