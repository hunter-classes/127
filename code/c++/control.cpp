#include <iostream>

int main()
{
  int a;
  a = 5;
  
  if (a < 20){
    std::cout << "a < 20\n";
    std::cout << "also in the true part\n";
  }

  if (a<20){
    std::cout << "if part: a < 20\n";
  } else {
    std::cout << "else part: a >= 20\n";
  }

  if (a < 10) {
    std::cout << "a < 10\n";
  } else if (a < 20){
    std::cout << "a < 20\n";
  } else {
    std::cout << "a >= 20\n";
  }
  
  std::cout << "outside the if\n";
  return 0;
}

