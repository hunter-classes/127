#include <iostream>
#include <ctime>
#include <cstdlib>


/*  return the sum of a[first]  plus a[second]  */
int add_two(int a[], int first, int second){
  int sum = a[first]+a[second];
  return sum;
  
}

void print_array(int a[], int size){
  for (int i = 0; i < size; ++i) {
    std::cout << "a[" << i << "]: " << a[i] << ", ";
  }
  std::cout << "\n";
}



int main(){
  int x = 100;
  int a[5]; // create an array that can store 5 ints.
  int y = 1000;

  
  
  std:: cout << "x: "<< x << "\n";
  std:: cout << "y: "<< y << "\n";


  for (int i = 0; i < 5; i++) {
    a[i] = 10+i;
  }

  int s = add_two(a,1,4);
  print_array(a,5);

  std::cout << s << "\n";

  /*
  for (int i = -2; i < 5; i++){
    a[i]=55;

  }

  std:: cout << "x: "<< x << "\n";
  for (int i = 0; i < 5; i++){
    std:: cout << "a[" << i << "]: " << a[i] << "\n";

  }
  std:: cout << "y: "<< y << "\n";

  */
  
  return 0;
}
