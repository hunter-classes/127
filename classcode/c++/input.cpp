#include <iostream>


int main()
{
  int guess;

  guess = 50;
  
  std::cout << "is " << guess << " your number?\n";

  int a,b;
  char c;
  // std::string s;
  // std::cin >> a >> b;

  // std::cout << "You entered " << a << " " << b << "\n";

  // std::cin >> s;
  // std::cout << "You entered " << s << "\n";

  std::string s;
  
  std::cout << "GETLINE EXAMPLE\n";
   getline(std::cin,s);
   std::cout << "You entered " << s << "\n";
  
    return 0;
}
