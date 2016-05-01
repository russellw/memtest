#include <stdio.h>
#include <stdlib.h>

static void help(void) { puts("Usage: memtest <gigabytes>"); }

int main(int argc, char **argv) {
  if (argc <= 1) {
    help();
    return 1;
  }
  size_t n = atof(argv[1]) * (1 << 30);
  if (!n) {
    help();
    return 1;
  }

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
