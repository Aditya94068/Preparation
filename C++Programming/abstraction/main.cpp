#include<iostream>
#include "bird.h"
using namespace std;
void birdDoSomething(Bird *bird)
{
  bird ->eat();
  bird ->fly();
}
int main()
{
Bird *bird = new sparrow();
birdDoSomething(bird);
cout<<"X"<<endl; 
return 0;
}