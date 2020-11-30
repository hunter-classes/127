#include <iostream> // kindof like import in python but different


// this is a single line comment

/*
  this is a multi
  line comment 
*/

// statements can only appear in functions!!!!
// you can't do this outside of a funciton:
// std::cout << "This isn't in a function\n";


// this is a a function in c++
// every c++ function NEEDS a funciton named main
// it is automatically run when you run your program.
int main()
{

  // semi colon ends statements
  std::cout << "Hello World!" << std::endl;
  std::cout << "This is a second line with an embedded newline\n";
  
  return 0;
}
