#include <iostream>


int main()
{
  int x = 21;
  double d = 21;
  char c;
  bool tf = false;
  std::string s = "this is a string";
  
  std::cout << "Hello World!\n";
  std::cout << "the var x = " << x << "\n";

  std::cout << "Doubles: "<< d << " " << d/2 << std::endl;
  std::cout << "Ints: "<< x << " " << x/2 << std::endl;

  c = 'x'; // a SINGLE character 
  std::cout<<c << "\n";

  std::cout << "A true value: " << tf << "\n";

  std::cout << s << "\n";
  return 0;
}
