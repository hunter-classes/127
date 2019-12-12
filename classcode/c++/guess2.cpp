#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::cin;


int main()
{

  srand(time(NULL));

  int number = rand()%100;
  int guess;
  
  while (true){
    cout << "Enter your guess:";
    cin >> guess;

    if (guess > number){
      cout << "Too high!\n";
    } else if (guess < number){
      cout << "Too low!\n";
    } else {
      cout << "You got it!\n";
      return 0;
	}

    
    
  }
  return 0;;
}
