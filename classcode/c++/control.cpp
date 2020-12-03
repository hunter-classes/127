#include <iostream>
#include <ostream>



int main()
{
  int a;
  int b;

  a = 20;
  b = 20;

  /*
   *
   if ( BOOLEAN IN PARENS)
     statement;

   if (BOOLEAN IN PARENS){
     statement 1;
     statement 2;
     ...
     statement n;
   } // don't need a ; here

   if (BOOLEAN)
     statement;
   else
     statement;

   if (BOOLEAN){
     statements;
   } else {
     statements;
   }

   if (BOOEAN){
     statemets;
   } else if (BOOLEAN2){
     statements;
   } // can keep having else if and an optional else at the end

*/
  
  if (a>b){
    std::cout << "a is greater\n"; 
    std::cout << "This is a second statement\n"; // <== not part of the if
  } else if (a<b){
    std::cout << "a is less\n";
  } else {
    std::cout << "They're equal\n";
  }


  /*
   *
   while (BOOLEAN IN PARENS)
     statement;

   while (BOOLEAN IN PARENS){
     statements
   }

*/

  int i=0;

  while (i < 10){
    std::cout << i << "\n";
    i++; // like i=i+1 but has some subtle differences  
  }

  char c='y';

  while (c!='n'){
    std::cout << "Do you want to play again (y,n)?: ";
    std::cin >> c;
    
    
  }
  
  std::string again="yes";
  while (again == "yes"){
    std::cout << "Do you want to play again (yes,no)?: ";
    std::cin >> again;
    
    
  }
  
  return 0;
}
