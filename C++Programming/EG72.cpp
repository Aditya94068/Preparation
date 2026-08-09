#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node(){
        this -> data = 0;
        this -> next = NULL;
    }
    Node(int data){
        this -> data = data;
        this -> next = NULL;
    }
};
void insertByValues(Node* &head,Node* &tail,int data,int value)
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
        if(temp ->data == value)
        {
            Node* newNode = new Node(data);
            newNode->next = temp->next;    
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
    Node* temp = head;
    while(temp != NULL)
    {
        cout<<temp -> data<<" ";
        temp = temp -> next;
    }
}
int main()
{
    Node* head = NULL;
    Node* tail = NULL;

    insertByValues(head,tail,10,10);
    insertByValues(head,tail,20,10);
    insertByValues(head,tail,30,10);
    insertByValues(head,tail,40,10);
    print(head);
}