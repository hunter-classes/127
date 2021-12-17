#include <cstdio>
#include <iostream>


int main()
{
  int a = 20;
  int b ,c;
  std::string d;
  char letter;
  bool tf;
  double decnumber;
  
  tf = false;
  
  letter = 'x';
  
  c = 10;
  b = a + c;

  d = "123";
  
  std::cout << tf << " " << letter << " "  << "b = " << b << "\n" ;
  std::cout << d << std::endl;

  // -> 1/3 will be INTEGER because 1 and 3 are integers
  //decnumber = 1/3;
  decnumber = 1.0*c/3;
  c = decnumber; // this truncates decnumber to an int
  std::cout << c << " " << decnumber << " " << decnumber * 3 << "\n";
  return 0;
}
