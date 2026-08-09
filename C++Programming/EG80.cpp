#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int data;
    Node* left;
    Node* right; 
    Node(int d)
    {
        this -> data = d;
        this -> left = NULL;
        this -> right = NULL;
    }
};
Node* buildTree(Node* root){
    cout<<"Enter the data :"<<endl;
    int data;
    cin>>data;
    if(data == -1)
    {
        return NULL;
    }
    root = new Node(data);
    cout<<"Enter data for inserting in left of :"<<data<<endl;
    root->left = buildTree(root->left);
    cout<<"Enter data for inserting in right of :"<<data<<endl;
    root->right = buildTree(root->right);
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
// void inOrder(Node* root)
// {
//     if(root == NULL)
//     {
//         return ;
//     }
//     inOrder(root->left);
//     cout<<root->data<<" ";
//     inOrder(root->right);
// }
vector<int> inOrder(Node* root)
{
    stack<Node*>st;
    Node* node = root;
    vector<int>arr;
    while(true)
    {
        if(node != NULL)
        {
            st.push(node);
            node = node->left;
        }
        else{
            if(st.empty()) break;
            node = st.top();
            st.pop();
            arr.push_back(node->data);
            node = node ->right;
        }
    }
    return arr;
}
void preOrder(Node* root)
{
    if(root == NULL)
    {
        return;
    }
    cout<<root->data<<" ";
    preOrder(root->left);
    preOrder(root->right);
}
void postOrder(Node* root)
{
    if(root == NULL)
    {
        return;
    }
    postOrder(root->left);
    postOrder(root->right);
    cout<<root->data<<" ";
}

int convertSumTree(Node* root)
{
    if(root == NULL)
    {
        return 0;
    }
    int leftVal = convertSumTree(root->left);
    int rightVal = convertSumTree(root->right);
    root->data = leftVal + root->data + rightVal;
    return root->data;
}
int main()
{

    Node* root = NULL;
    root = buildTree(root);
    //1 3 7 -1 -1 11 -1 -1  5 17 -1 -1 -1 
    // levelOrderTraversal(root);
    // vector<int>ans = inOrder(root);
    // for(int i = 0;i<ans.size();i++)
    // {
    //     cout<<ans[i]<<" ";
    // }
    // cout<<endl;
    // preOrder(root);
    // cout<<endl;
    // postOrder(root);
    convertSumTree(root);
    preOrder(root);
    return 0;
}