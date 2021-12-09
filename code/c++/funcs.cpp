#include <cstdio>
#include <iostream>

// c++ functions ALWAYS need a return type;
// void is if you don't want to return a value
void greet(){
  std::cout << "Hello from the greeter" << std::endl;
}

/*
  def greet():
      print("hello")
*/

int main()
{
  greet();
    
  return 0;
}

