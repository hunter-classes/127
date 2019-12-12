#include <iostream>
int main()
{
  int i;
  i=0;
  while (i < 10){
    std::cout << i << "\n";
    i++;
  }

  /*
    for (A ; B ; C ){

    }

    A <-- initialize - do this before the loop
    B <-- the boolean test - conditions to continue looping
    C <-- the thing to do at the bottom
  */

  for(i=0;i<10;i++){
    std::cout << i << "\n";
  }

  
  for (int j=100 ; j < 110 ; j++){
    std::cout << j << "\n";
  }

  //  std::cout << "\n" << j << "\n";

  i=5000;
  do{
    std::cout << i << "\n";
    i++;
  }while(i<5010);

  //int a[5]; // will fill with random values
  int a[5] = {10,3,20,4,15};
  

  for (i = 0; i < 4; ++i) {
    std::cout << "a[" << i  << "] = " << a[i] << "\n";
  }
  std::cout << "\n";

  a[2]=a[0]+5;
  
  for (i = 0; i < 4; ++i) {
    std::cout << "a[" << i  << "] = " << a[i] << "\n";
  }
  std::cout << "\n";

  std::string s = "Hello";
  for (i = 0; i < s.length(); ++i) {
    std::cout << s[i] << "\n";
  }

  s[2]='Z';
  for (i = 0; i < s.length(); ++i) {
    std::cout << s[i] << "\n";
  }

  return 0;
}
