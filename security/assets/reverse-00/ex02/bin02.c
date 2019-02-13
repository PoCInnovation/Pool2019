#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, const char *const argv[]) {
  if (argc < 2) {
    fprintf(stderr, "I want a password as argument.\n");
    return EXIT_FAILURE;
  }

  ++argv;
  if (strcmp(*argv, "quoi_de_neuf_docteur") == 0) {
    printf("C'est bingo !\n");
    return EXIT_SUCCESS;
  }

  printf("Non, c'est pas bon...\n");
  return EXIT_FAILURE;
}

// clang -O0 -m32 bin02.c -o bin02