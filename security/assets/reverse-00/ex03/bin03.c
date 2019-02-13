#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, const char *const argv[]) {
  if (argc < 2) {
    printf("Passe un argument, non ?\n");
    return EXIT_FAILURE;
  }

  ++argv;

  char *flag = strdup("avec_effet_de_serre");
  if (!flag) {
    printf("Dans quel monde vivons-nous ?\n");
    return EXIT_FAILURE;
  }

  size_t flagLen = strlen(flag);
  for (size_t i = 0; i < flagLen; ++i) {
    if (flag[i] == '_') continue;
    flag[i] -= 32;
  }

  if (strcmp(*argv, flag) == 0) {
    printf("C'est bon !\n");

    free(flag);
    return EXIT_SUCCESS;
  }

  printf("Tellement pas...\n");
  free(flag);
  return EXIT_FAILURE;
}

// clang -O0 -m32 bin03.c -o bin03