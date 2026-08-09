#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class Node{
    public:
    int data;
    Node* left;
    Node* right;
    Node(int data){
        this->data = data;
        this ->left = NULL;
        this ->right = NULL;
    }
};
int findPosition(int arr[], int n,int element)
{
    for(int i = 0;i<n;i++)
    {
        if(arr[i] == element){
            return i;
        }
    }
    return -1;
}
//Build tree from inorder and preorder traversal
Node* buildTreeFromPreorderInorder(int inorder[],  int preorder[],int size,int& preIndex,int inorderStart,int inorderEnd)
{
    //base case
    if(preIndex >= size || inorderStart > inorderEnd){
        return NULL;
    }
    //Step A
    int element = preorder[preIndex++]; 
    Node* root = new Node(element);
    int pos = findPosition(inorder,size,element);
    //Step B : root ->left solve
    root->left = buildTreeFromPreorderInorder(inorder,preorder,size,preIndex,inorderStart,pos-1);
    //Step C : root ->right solve  
    root->right = buildTreeFromPreorderInorder(inorder,preorder,size,preIndex,pos+1,inorderEnd);
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
int main(){
    int inOrder[] = {40,20,50,10,60,30,70};
    int preOrder[] = {10,20,40,50,30,60,70};
    int size = 7;
    int preIndex = 0;
    int inorderStart = 0;
    int inorderEnd = size - 1;
    Node* root = buildTreeFromPreorderInorder(inOrder,preOrder,size,preIndex,inorderStart,inorderEnd);
    cout<<"Printing Level Order Traversal"<<endl;
    levelOrderTraversal(root);
}