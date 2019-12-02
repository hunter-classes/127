#include <iostream>


int main(){
  int a = 20;
  int b,c;
  double e,f,g;

  
  bool truth_val;
  truth_val = false; // or true

  /* this is a 
     multiline comment */
  
  char ch;
  ch = 'q'; // char are single characters - use single quotes
  
  std::string s = "This is a string";
  
  b = 30;
  c = a + b;
  
  std::cout << s << " - Hello world! - " << ch << " : "<< 'x'<< ":"
	    << truth_val << " : " << 123.45 << std::endl;
  std::cout << "Line two ";
  std::cout << "Also line 2\n";

  std::cout << c << "\n";
  std::cout << c + b << "\n";

  a = 10;
  b = 3;
  c = a/b;
  std::cout <<  a << " / " << b << " = " << c << "\n";

  e = 10;
  f = 3;
  g = e/f;
  std::cout <<  e << " / " << f << " = " << g << "\n";
  
  return 0;
}



