#include <iostream>


/*
  variables are available in the scope (function) in which they
  are declared. You can use the same name in different scopes (but
  be careful about that).

  Parameters are passed value <-- the parameter gets a COPY of the value
  from the caller. If the parameter is changed in the function it is
  only the copy that's changed. The variable in the caller is
  not affected.

*/
int add_two_numbers(int a, int b){
  int c;
  c = a + b;
  a = 5000;
  b = 3000;
  
  std::cout << "add func: "<< a << " , " << b << " , " << c << "\n";
  return c;

}

void printstuff(){
  std::cout << "this function just prints stuff\n";
  return; // this returns immediately. The last line won't be executed
  std::cout << "It doesn't return any values <-- we use void for that\n";
  
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

  std::cout << "Main: " << a << " , " << b << " , " << c << "\n";

  printstuff();
  
  return 0;
}
    
