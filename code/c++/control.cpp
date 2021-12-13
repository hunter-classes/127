#include <iostream>



int main()
{
  int a;

  a=6;
  if (a>5){
    std::cout << "a is greater than 5\n";
    std::cout << "This is also in the if\n";
  } else if (a == 4){
    std::cout << "a is 4\n";
  } else {
    std::cout << "This is in the else\n";
    std::cout << "so is this\n";
  }
  
  std::cout << "after the if\n";

  
  return 0;
}
