#include <iostream>


/*  Anatomy of a C++ function

    return_type name(parameters){

    code
    code
    code 
    
    return a_value_of_the_return_type
    }


*/


std::string hello(){
  return "Hello";
}


int main()
{

  int a;
  int b = 30;
  
  a = 20;

  b = b + a;

  b = b + 20.34;

  // You can't redeclare a variable a second time in a function
  // you can reassign a value but you can't redeclare it to
  // be another type
  // double b = 123.45;
  
  std::cout << "The value of a is " << a << "\n";
  std::cout << "The value of b is " << b << "\n";

  double d1, d2;

  d1 = 20/3; // this becoome 6 not 6.something
  // 20 is an int, 3 is an int so c++
  // says do division (/) on two ints which is an int

  // we can force it into a float or double context
  // to do the division we want
  d2 = 20.0 / 3;
  

  std::cout << d1 << "\n";
  std::cout << d2 << "\n";

  char c; // c holds a single character which we
          // write in single quotes.

  c = 'a';

  std::string s = "hello";


  std::cout << c << " "  << s << "\n";

  // c++  math stuff is mostly like Python
  // + - * / = != > < >= <= 

    std::cout << hello() << hello() << hello() << std::endl;
    
  return 0;
}
