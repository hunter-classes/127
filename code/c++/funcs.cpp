#include <iostream>

// use void as the return type
// if you're not going to
// return a value
// you can still use the return statement
// just without any value
// just "return"
void print_hello(){
  std::cout << "Hello world\n";
}

int add_two_numbers(int a, int b){
  int c;
  std::cout << "In func a: " << a << " b: " << b << "\n";
  c = a + b;
  return c;
}


int main()
{
  int a, b;
  print_hello();
  int result = add_two_numbers(5,8);
  a = 30;
  b = 100;
  result = add_two_numbers(b,a);
  std::cout << "a: " << a << " b: " << b << "\n";
  std::cout << result << "\n";
  return 0;
}
