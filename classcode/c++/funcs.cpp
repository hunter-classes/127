#include <iostream>

int add_two_numbers(int a, int b){
  int c;
  c = a + b;
  a = 5000;
  b = 3000;
  

  return c;

}

int main()
{
  int x, y;
  int z;
  x = 20;
  y = 30;

  
  z = add_two_numbers(x,y);
  std::cout << x << " + " << y << " = " << z << "\n";

  int a = 100, b = 200;

  int c = 3;

  std::cout << a << " , " << b << " , " << c << "\n";

  c = add_two_numbers(a,b);

  std::cout << a << " , " << b << " , " << c << "\n";

  return 0;
}
    
