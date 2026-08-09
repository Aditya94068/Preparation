#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next ;
    Node()
    {
        this->data = 0;
        this->next = NULL;
    }
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};
void print(Node *head)
{
    Node* temp = head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp = temp->next;
    }
}
void insertnewNode(Node *& head,Node *& tail,int data)
{
    if(head == NULL)
    {
        Node*newNode = new Node(data);
        head = newNode;
        tail = newNode;

    }
    else{
    Node* newNode = new Node(data);
    newNode->next = head;
    head = newNode;
    }
}
void insertNewNodeTail(Node* &head,Node* &tail,int data)
{
    if(head == NULL)
    {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
    }
    else{
        Node* newNode = new Node(data);
        tail->next = newNode;
        tail = newNode;
    }
}
int main()
{   
    // Node* first = new Node(10);
    // Node* second = new Node(20);
    // Node* third = new Node(30);
    // Node* fourth = new Node(40);
    // Node* fifth = new Node(50);
    // first ->  next = second;
    // second -> next = third;
    // third ->next = fourth; 
    // fourth -> next = fifth;
    // print(first);
    Node* head = NULL;
    Node* tail = NULL;
    insertnewNode(head,tail,20);
    insertnewNode(head,tail,30);
    insertnewNode(head,tail,40);
    insertnewNode(head,tail,50);
    insertnewNode(head,tail,60);
    insertNewNodeTail(head,tail,77);
    insertNewNodeTail(head,tail,100);
    print(head);

    return 0;
}