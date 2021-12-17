#include <iostream>




bool isRightTriangle(int a, int b, int c){

  if (a*a + b*b == c*c){
    return true;
  } else {
    return false;
  }
}

// This is shorter. Since the above if just returns true if the
// expression is true and false if it's false you don't actually
// need the if.
bool isRightTriangleShorter(int a, int b, int c){
  return a*a+b*b==c*c;
}

std::string fizzbuzz(int i){
  std::string result;

  result = std::to_string(i);
  if (i%3 == 0 && i%5 == 0) {
    result = "FizzBuzz";
  } else if (i%3 == 0) {
    result = "Fizz";
  } else if (i%5 == 0) {
    result = "Buzz";
  } else {
    // I didn't specify what to do for this case in the
    // question so anything reasonable was fine.
    result = "FOOF";
  }

  return result;
  
}


int main()
{

  std::cout << "------------------- isRightTriangle -------------\n";
  std::cout << "3 4 5 : " << isRightTriangle(3,4,5) << "\n";
  std::cout << "3 4 6 : " << isRightTriangle(3,4,6) << "\n";
  std::cout << "3 4 5 : " << isRightTriangleShorter(3,4,5) << "\n";
  std::cout << "3 4 6 : " << isRightTriangleShorter (3,4,6) << "\n";

  std::cout << "\n";
  std::cout << "------------------- isRightTriangle -------------\n";

  int i;
  for (i=1; i < 22; i++){
    std::cout << std::to_string(i) + ": " << fizzbuzz(i) << std::endl;
  }
  
  return 0;
}
