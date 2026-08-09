#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int data;
    Node* left;
    Node* right;
    Node(int data)
    {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};
Node* insertIntoBST(Node* root,int data)
{
    // TIme Complexity : Average case := O(logn) , worst case :- O(height) means O(n); 
    if(root == NULL)
    {
        // this is the first node we have to create
        root = new Node(data);
        return root;
    }
    //no the first node
    if(root -> data > data)
    {
        // insert into left
        root->left = insertIntoBST(root->left,data);
    }
    else{
        // insert into right
        root->right = insertIntoBST(root->right,data);
    }
    return root;
}

void levelOrderTraversal(Node* root)
{
    queue<Node*> q;
    q.push(root);
    q.push(NULL);
    while(!q.empty())
    {
        Node* temp =  q.front();
        q.pop();
        if(temp == NULL){//purana level complete traverse ho chuka hai
            cout<<endl;
            if(!q.empty())//queue still has some child nodes
            {
                    q.push(NULL);
            }
        }
        else{
            cout<<temp -> data <<" ";
            if(temp ->left){
                q.push(temp -> left);
            }
            if(temp->right)
            {
                q.push(temp->right);
            }
        }
    }
}
void inorder(Node* root)
{
    // Inorder of the bst is always sorted  
    if(root == NULL)
    {
        return;
    }
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
}
void preorder(Node* root)
{
    if(root == NULL)
    {
        return;
    }
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right);
}
void postorder(Node* root)
{
    if(root == NULL)
    {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout<<root->data<<" ";
}
void takeInput(Node*&root)
{
    int data;
    cin >> data;
    while(data != -1)
    {
        root = insertIntoBST(root,data);
        cin>>data;
    }
}
int main(){
    Node* root = NULL;
    cout<<"Enter the data for Node"<<endl;
    takeInput(root);
    cout<<"Printing tree"<<endl;
    levelOrderTraversal(root);
    cout<<endl;

    cout<<"Inorder"<<endl;
    inorder(root);
    cout<<endl;
    cout<<"preorder"<<endl;
    preorder(root);
    cout<<endl;
    cout<<"postorder"<<endl;
    postorder(root);
    return 0;
}