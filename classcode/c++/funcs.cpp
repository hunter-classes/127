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

  /* C++ boolean comparators
     >
     <
     >=
     <=
     == 
     !=  not equals
     && and
     || or
     !  not 

  */
  int a = 0;
  // if (a == 0){
  //   std::cout << "The if is true: " << a << std::endl;
  // }
  // std::cout << "After the if statement: " << a << std::endl;

  a=22;
  // if (a<10){
  //   std::cout << "A is less than 10\n";
  // }

  // if (a<10){
  //   std::cout << "A is less than 10\n";
  // } else {
  //   std::cout << "A is greater or equal to  10\n";
  //}

  a=10;
  if (a<10){
    std::cout << "A is less than 10\n";
  } else if (a==10){
    std::cout << "A is equal to 10\n";
  } else {
    std::cout << "A is greater than  10\n";
  }
  
  std::cout << "This is after the if statement\n";


  int i=0;
  while (i < 10){
    std::cout << i << " " << add2(i,i) << "\n";
    ++i; // there's also --i or i--
  }


  // std::cout << "\n\n";
  // a=10;
  // std::cout << a << "\n";
  // if (++a ==  10){
  //   std::cout << "A had to be 10 " << a << "\n";

  // }
  // std::cout << a << "\n";
  
  return 0;
}
