#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

int part1(){
  for (int a = 0; a <= 9; a++) {
    char string_A[10];
    sprintf(string_A, "%d", a);
    mkdir(string_A, 0755);
  }
  
  return 0;
}

int part2(){
  for (int a = 0; a <= 9; a++) {
    for (int b = 0; b <= 9; b++) {
      char string_AB[10];
      sprintf(string_AB, "%d/%d", a, b);
      mkdir(string_AB, 0755);
    }
  }
  
  return 0;
}

int part3(){
  for (int a = 0; a <= 9; a++) {
    for (int b = 0; b <= 9; b++) {
      for (int c = 0; c <= 9; c++) {
        char string_ABC[10];
        sprintf(string_ABC, "%d/%d/%d", a, b, c);
        mkdir(string_ABC, 0755);
      }
    }
  }
  
  return 0;
}

int part4(){
  for (int a = 0; a <= 9; a++) {
    for (int b = 0; b <= 9; b++) {
      for (int c = 0; c <= 9; c++) {
        for (int d = 0; d <= 9; d++) {
        char string_ABCD[10];
        char filename[25];
        sprintf(string_ABCD, "%d/%d/%d/%d", a, b, c, d);
        sprintf(filename, "%s/.combo", string_ABCD);
        mkdir(string_ABCD, 0755);
        fopen(filename, "w");
      }
      }
    }
  }
  
  return 0;

}

int main() {
  part1();
  printf("1/4 complete\n");
  part2();
  printf("2/4 complete\n");
  part3();
  printf("3/4 complete\n");
  part4();
  printf("4/4 complete\n");
  
  return 0;
}