#include<iostream>
using namespace std;
// class Heap{
//     public:
//     int* arr;
//     int size;
//     Heap(int size)
//     {
//         this->size = size;
//         arr = new int[size];
//     }
//     void insert(int value)
//     {

//     }
// };
class Heap{
    public:
    int arr[101];
    int size;
    Heap()
    {
        size = 0;
    }
    void insert(int value)
    {
        //value insert karo end me
        size = size + 1;
        int index = size;
        arr[index] = value;
        //iss value ko place at right{correct position} position
        while(index > 1)
        {
            int parentIndex = index / 2;
            if(arr[index] > arr[parentIndex])
            {
                swap(arr[index], arr[parentIndex]);
                index = parentIndex;
            }
            else{
                break;
            }
        }
    }
    void deleteFromHeap(){
        if(size == 0)
        {
            cout<<"Nothing  to delete"<<endl;
        }
        //replace root node value  with last node  data
        arr[1] =    arr[size];
        size--;
        //place root node data on its correct position
        int i = 1;
        while(i < size){
            int leftIndex = 2 * i;
            int rightIndex = 2 * i + 1;
            if(leftIndex < size && arr[i] < arr[leftIndex])
            {
                swap(arr[i],arr[leftIndex]);
                i = leftIndex;
            }
            else if(rightIndex < size && arr[i] < arr[rightIndex])
            {
                swap(arr[i] , arr[rightIndex]);
                i = rightIndex; 

            }
            else{
                return;
            }
        }
    }
};
int main()
{
    Heap h;
    h.arr[0] = -1;
    h.arr[1] = 100;
    h.arr[2] = 50;
    h.arr[3] = 60;
    h.arr[4] = 40;  
    h.arr[5] = 45;
    h.size = 5;
    cout<<"Printing the heap"<<endl;
    for(int i = 1;i<=h.size;i++)
    {
        cout<<h.arr[i]<<" ";
    }
    cout<<endl;
    h.insert(110);
    cout<<endl<<"Printing the heap"<<endl;
    for(int i = 1;i<=h.size;i++)
    {
        cout<<h.arr[i]<<" ";
    }
    cout<<endl;
    h.deleteFromHeap();
    cout<<"Deleting value"<<endl;
    for(int i = 1;i<=h.size;i++)
    {
        cout<<h.arr[i]<<" ";
    }

    return 0;
}