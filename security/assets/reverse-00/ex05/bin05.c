#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static const char *crabRave = "c'est pas le quartier qui me quitte"
                              ", c'est moi j'quitte le quartier";


static size_t partyHard(const char *s1, const char *s2) {
  while (*s1 == *s2) {
    if (*s1 == '\0') return EXIT_SUCCESS;
    ++s1; ++s2;
  }

  return *s1 - *s2;
}

int main(int argc, const char *const argv[]) {
  if (argc < 2) {
    printf("Il faut un argument...\n");
    return EXIT_FAILURE;
  }

  ++argv;

  if (partyHard(crabRave + 37, *argv) == 0) {
    printf("C'est correct !\n");
    return EXIT_FAILURE;
  }

  printf("Ce n'est pas correct...\n");
  return EXIT_SUCCESS;
}

// gcc -O0 -m32 -s bin05.c -o bin05
