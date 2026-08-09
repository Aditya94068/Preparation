#include<iostream> 
using namespace std;
class Node{
    public : 
    int data;
    Node *next;
    Node(){
        this->data = 0;
        this ->next = NULL;
    }  
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};
void print(Node* head)
{

    Node* temp = head;
    while(temp != NULL)
    {
        cout<<temp->data<<" ";
        temp = temp -> next;
    }
}
void attachNodeOnHead(Node* &head,Node* &tail,int data)
{
    if(head == NULL)
    {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
        return;
    }
    else{
    Node* newNode = new Node(data);
    newNode->next = head;
    head = newNode;
    }
}
void attachNodeOnTail(Node* &head,Node* &tail,int data)
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
int findLen(Node* head)
{
    Node* temp = head;
    int len = 0;
    while(temp != NULL)
    {
        temp = temp -> next;
        len++;
    }
    return len;
}
void attachAtPosition(int data,int position,Node* &head,Node* &tail){
    if(head == NULL)
    {
        Node* newNode = new Node(data);
        head = newNode;
        tail = newNode;
        return;
    }
    if(position == 0)
    {
        attachNodeOnHead(head,tail,data);
        return;
    }
    int len = findLen(head);
    if(position >= len)
    {
        attachNodeOnTail(head,tail,data);
        return;
    }
    Node* prev = head;
    int i = 1;
    while(i<position)
    {
        prev = prev -> next;
        i++;
    }
    Node* curr = prev -> next;
    Node* newNode = new Node(data);
    newNode-> next = curr;
    prev->next = newNode;
}   

void deleteNode(int position ,Node* &head,Node* &tail)
{
    if(head == NULL)
    {
        cout<<"Cannot Delete LL is empty"<<endl;
        return;
    }
    if(position == 1)
    {
        Node* temp = head;
        head = head ->next;
        temp -> next = NULL;
        delete temp;
    }
    int len = findLen(head);
    if(position==len)
    {
        int i = 1;
        Node* prev = head;
        while(i<position-1)
        {
            prev = prev -> next;
            i++;
        }
        prev -> next = NULL;
        Node *temp = tail;
        tail = prev;
        delete temp;
        return;
    }
    int i = 1;
    Node *prev = head;
    while(i<position-1)
    {   
        prev = prev ->next;
        i++;
    }
    Node* curr = prev->next;
    prev->next= curr->next;
    curr->next = NULL;
    delete curr;

}
int main()
{
    // Node *head = new Node(10);
    // Node *head2 = new Node(20);
    // Node *head3 = new Node(30);
    // head -> next = head2;
    // head2 ->  next = head3;

    // Node* head = new Node(100);
    // Node* second = new Node(200);
    // head -> next = second;
    // Node* temp = head;
    // Node* temp2 = temp -> next;
    // cout<<temp2 -> data<<endl;
    Node* head = NULL;
    Node* tail = NULL;
    attachNodeOnHead(head,tail,10);
    attachNodeOnHead(head,tail,20);
    attachNodeOnHead(head,tail,30);
    attachNodeOnHead(head,tail,40);
    attachNodeOnTail(head,tail,100);
    // attachNodeOnTail(head,tail,100);
    // attachAtPosition(101,2,head,tail);
    print(head);
    cout<<endl;
    deleteNode(3,head,tail);
    print(head);
    
}