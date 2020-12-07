#include <iostream>


int main(){

  int i;

  i = 0; // <-- initialize the loop 
  while (i<10){ // <--- in the parens we have the test
    std::cout << i << ", ";
    i=i+1; // <--thing to change so the boolean eventuall exits
  }
  std::cout << "\n";

  /*
   *
   initiailize
   while (boolean to keep looping){
     stuff;
     change so that boolean will eventually exit
  }


  for(initialize;boolean;change){
    stuff;
  }
  */

  for (i = 0 ; i < 10 ; i++){
    std::cout << i << ", ";
  }
  std::cout << "\n";


  for(int secret=20; secret != 100; std::cin >>secret){
    std::cout << "You entered " << secret <<"\n";    
  }

  i = 100;
  for ( ; i > 5 ; i=i-4){
    std::cout << i << ", ";    
  }
  std::cout << "\n";

  
}

