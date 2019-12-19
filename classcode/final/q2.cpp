#include <iostream>
int main()
{
  int sum = 0;
  int sqnum;
  for (int i = 0; i <= 101; ++i) {
    sqnum = i*i;
    if (sqnum % 2 == 0 && sqnum % 3 == 0){
      sum = sum + sqnum;
    }
  }
  std::cout << sum << "\n";
  
  return 0;
}
