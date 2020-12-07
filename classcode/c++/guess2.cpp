#include <iostream>


int main()
{
  srand(time(0));
  int r=rand();
  char response;
  int guess=50;
  int guesses = 0;
  while (response != 'c'){
    std::cout << "My guess is: " << guess << "\n";
    std::cout << "How'd I do (h,l,c)?";
    std::cin >> response;

    if (response == 'h'){
      guess = (100 - guess)/2;
      
    } else if (response == 'l'){
      guess = guess /2;
      
    }
    guesses++;
  }

  std::cout << "I got it in " << guesses << " guesses!\n";
  return 0;
}
