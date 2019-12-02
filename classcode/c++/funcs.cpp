#include <iostream>
/*

  Python Function: 
  def name(params):
  line
  line
  line
  return something

  def add2(a,b):
    c = a+b
    return c
*/

int add2(int a, int b){
  int i;
  i = a + b;
  return i;
}


int main()
{
  std::cout << "3 + 5 = " << add2(3,5) << std::endl;

  /* 
     Python loop to count to 10

     i = 0
     while i < 10:
       print(i);
       i = i + 1
  */
  int i=0;
  while (i < 10){
    std::cout << i << " " << add2(i,i) << "\n";
    i=i+1;
  }

  
  return 0;
}
