#include <iostream>
#include <ostream>

// This is bad: using namespace std;

// This is better - explicitly
// use specific functions
//using std::cout;
// using std::endl;

// but best is just don't do either

int main()
{

  std::cout << "hello world" << std::endl;
  return 0;
}
