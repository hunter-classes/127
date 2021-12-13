#include <iostream>

void if_example(){
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


}

void while_example(){
  int i;

  i = 0;
  while (i < 20) {
    std::cout << i << std::endl;
    i = i + 1;
    if (i == 10){
      break; // break exits the loop imediately
      // if we put return in here it would hvae
      // returned imediately

    }
  }
  std::cout << "After the loop\n";
  
}

int main()
{

  // if_example();

  while_example();
  
  return 0;
}
