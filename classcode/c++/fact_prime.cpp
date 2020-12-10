#include <iostream>
#include "math.h" // need this for sqrt

int fact(int n){
  int prod = 1;
  for (int i=1; i <= n; i++){
    prod = prod * i;
  }
  return prod;
}

bool is_prime(int n){
  if (n==1 || n==2)
    return true;

  // could also go to n/2 or even n-1
  for (int i = 2; i <= sqrt(n); i++){
    if (n%i==0){
      return false;
    }
  }
  return true;
  
}

int main()
{
  for (int i = 0; i < 10; i++){
    std::cout << i << "! = "<< fact(i) << "\n";
    
  }

  std::cout << "\n\n";
  for (int i = 1; i < 100; i++){
    if (is_prime(i)){
      std::cout << i << "\n";
    }

  }  
  return 0;
}
