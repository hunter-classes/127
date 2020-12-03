#include <iostream>


int main()
{
  srand(time(0));
  int r=rand();

  std::cout << r << "\n";

  int i =0;
  while (i<10){
    r = rand()%100;
    std::cout << r << "\n";
    i++;
    
  }
  return 0;
}
