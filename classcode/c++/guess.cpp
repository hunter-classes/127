#include <iostream>

using std::cout;
using std::cin;


int main()
{

  
  int guess = 50;
  char correct='n';
  
  while (true){
    std::cout << "Is the number " << guess << "?\n";
    std::cout << "y/h/l\n\n";
    std::cin >> correct;
    if (correct=='h'){
      guess = guess / 2;
    } else if (correct=='l'){
      guess = guess + (guess / 2);
    } else {
      std::cout << "I WIN!!!!\n";
      return 0;
    }
  }
  return 0;
}
