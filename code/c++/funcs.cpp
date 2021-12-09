#include <cstdio>
#include <iostream>

// c++ functions ALWAYS need a return type;
// void is if you don't want to return a value
void greet(){
  std::cout << "Hello from the greeter" << std::endl;
}


// parametes are in the parens but need the type
void personal_greeter(std::string name){
  std::cout << "Hello " << name << "!" << "\n";
}

/*
  def greet(name):
  print("hello",name)
*/

int main()
{
  greet();
  personal_greeter("Thomas");
  return 0;
}

