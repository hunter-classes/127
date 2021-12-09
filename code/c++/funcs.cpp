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

// using a return type - this returns one more than x (increment)
int inc(int x){
  int b = x + 1;
  return b;
}

// force an integer division on two doubles
// note this is returning an int
int int_div(double a, double b){
  int result;
  result = int(a) / int(b);
  return result;
}

int main()
{
  greet();
  personal_greeter("Thomas");
  int input = 20;
  int output;
  output = inc(input);
  std::cout << output << " is one more than " << input << "!\n";

  double a = 50.3;
  double b = 25.5;
  int intdiv = int_div(a,b);
  std::cout << a << "/" << b << " is " << a/b << "\n";
  std::cout << a << " int_div " << b << " is " << intdiv << "\n";
  
  return 0;
}

