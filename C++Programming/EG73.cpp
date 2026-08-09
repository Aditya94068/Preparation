#include<iostream>
using namespace std;
class Node{
    public:
    int data ;
    Node* next ;
    Node()
    {
        this->data = 0;
        this -> next = NULL;
    }
    Node(int data){
        this -> data = data;
        this->next = NULL;
    }
};
void insertAthead(Node* &head,Node* &tail,int data)
{
     if(head == NULL)
     {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
     }
     else{
        Node* newNode = new Node(data);
        newNode -> next = head;
        head = newNode;
     }
}
void insertAtTail(Node* &head,Node* &tail,int data)
{
    if(head == NULL){
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
    }
    else{
        Node* newNode = new Node(data);
        tail -> next = newNode;
        tail = newNode;
    }
}
int getLength(Node* &head)
{
    int len = 0;
    Node* temp = head;
    while(temp != NULL)
    {
        len++;
        temp = temp -> next;
    }
    return len;
}
void insertAtPosition(Node* &head,Node* &tail,int position ,int data)
{
    if(head == NULL)
    {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
        return;
    }
    if(position == 0){
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
        return;
    }
    int len = getLength(head);
    if(position >= len)
    {
        Node* newNode = new Node(data);
        tail -> next = newNode;
        tail = newNode;
        return;
    }
    Node* newNode = new Node(data);
    Node* prev = head;
    int i = 0;
    while(i < position-1)
    {
        prev = prev -> next;
        i++;
    }
    newNode ->next = prev->next;
    prev->next = newNode;
    return;
}
void insertAtValue(Node* &head,Node* &tail,int value,int data)
{
    if(head == NULL)
    {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
        return;
        
    }
    Node* temp = head;
    while(temp != NULL)
    {
        if(temp->data == value)
        {
            Node* newNode = new Node(data);
            newNode -> next = temp -> next;
            temp -> next = newNode;
            if(temp == tail)
            {
                tail = newNode;
            }
            return;
        }   
        temp = temp -> next;
    }
}

void print(Node* head)
{
    Node*temp = head;
    while(temp != NULL)
    {
        cout<<temp->data<<" ";
        temp = temp -> next;
    }
}
int main()
{
    Node* head = NULL;
    Node* tail = NULL;
    insertAthead(head,tail,30);
    // insertAthead(head,tail,30);
    // insertAthead(head,tail,30);
    // insertAthead(head,tail,30);
    insertAtTail(head,tail,100);
    insertAtTail(head,tail,100);
    insertAtTail(head,tail,200);
    // insertAtPosition(head,tail,1,50);
    // insertAtPosition(head,tail,6,23);
    insertAtPosition(head,tail,3,23);
    insertAtValue(head,tail,23,60);
    print(head);
    return 0;
}