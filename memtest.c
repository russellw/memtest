#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  size_t n = atof(argv[1]) * (1 << 30);

  char *p = malloc(n);
  if (!p) {
    perror("malloc");
    exit(1);
  }

  memset(p, 1, n);
  size_t a = 0;
  for (size_t i = 0; i < n; i++)
    a += p[i];
  if (a != n) {
    puts("error");
    return 1;
  }

  return 0;
}
