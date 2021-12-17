#include <iostream>

int main()
{
  int a,b;
  std::cout << "Enter a:";
  std::cin >> a;

  std::cout << "Enter b:";
  std::cin >> b;

  std::cout << "You entered " << a << " for a\n";
  std::cout << "and " << b << " for b.\n";

  if (a>b){
    std::cout << "a is greater than b.\n";
  } else {
    std::cout << "b is greater or equal to a.\n";
  }
  return 0;
}
