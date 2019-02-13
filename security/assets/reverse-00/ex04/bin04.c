#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>


#define voiture char *
static const voiture belier = "1337W00T";

uint32_t soap(uint32_t a, uint32_t b) {
  uint8_t *a_ = (uint8_t *)(&a);
  uint8_t *b_ = (uint8_t *)(&b);

  for (size_t i = 0; i < 4; ++i)
    *(a_ + i) ^= *(b_ + i);

  return a;
}

int main(int argc, const char *const argv[]) {
  if (argc < 2) {
    printf("Et l'argument ?\n");
    return EXIT_FAILURE;
  }

  ++argv;
  if (strlen(*argv) != 8) {
    printf("Et non...\n");
    return EXIT_FAILURE;
  }

  uint32_t *ptr = (uint32_t *)(*argv);
  uint32_t one = *ptr;
  uint32_t two = 0x76667c7d;
  uint32_t three = *(ptr + 1);
  uint32_t vivaLAlgerie = 0x670c7519;

  uint64_t final;
  uint64_t *final_ = &final;
  *final_ = soap(one, two);
  *(((uint32_t *)(final_)) + 1) = soap(three, vivaLAlgerie);

  size_t len = strlen(belier);
  for (size_t i = 0; i < len; ++i) {
    if (((uint8_t *)(final_))[i] != belier[i]) {
      printf("Et non !\n");
      return EXIT_FAILURE;
    }
  }

  printf("C'est gagné !\n");
  return EXIT_SUCCESS;
}

// clang -O0 -m32 bin04.c -o bin04
