#include <stdio.h>
#include <stdlib.h>


int main() {
  int32_t i = 0;
  i += 12;

  if (i == 18) {
    printf("Ah bon ?\n");
  }

  printf("Hello, World !\n");
  return EXIT_SUCCESS;
}

// clang -O0 -m32 bin01.c -o bin01