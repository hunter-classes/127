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

void do_example(){
  int i=10;
  do {
    std::cout << i << std::endl;
    i--;
    
  } while (i > 0);
}

// This is the for COUNTING loop
void for_example(){
  // for (start value ; boolean test to keep looping ; change expression)
  int i;
  for (i = 0; i < 10 ; i=i+1){
    std::cout << i << "\n";
  }

  std::cout << "\n\n";
  
  // Notice we can declare the variable in the for
  // but it will be created when the for executs
  // and it will be destroyed when the loop exits
  for (int a = 10; a > 0 ;    a = a - 2){
  
    std::cout << "a is " << a << "\t";

    
  }
  std::cout << "\n";
  
  

}

int main()
{

  // if_example();

  // while_example();

  // do_example();
  
  for_example();
  
  return 0;
}
