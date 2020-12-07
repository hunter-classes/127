#include <iostream>


int main()
{
  srand(time(0));
  int secret=rand();
  int guess;
  
  secret = rand()%100;
  guess = secret + 1; // this way we know we'll enter the loop

  std::cout << "CHEAT: " << secret << "\n";
  while (guess != secret){
    std::cout << "Please enter a guess between 0 and 99:";
    std::cin >> guess;
    if (guess > secret){
      std::cout << "Your guess is too high.\n";
    }
    else{
      std::cout << "Your guess is too low.\n";
    }
    
    
  }

  
  return 0;
}
