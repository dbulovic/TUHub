#include <stdio.h>

int main(int argc, char* argv[]) {
  int wants_argument = 1, has_argument = 0;
  if(argc == 2)
    if(wants_argument == 1)
      has_argument = 1;
  else
     printf("wrong number of arguments (must be 1)!\n");
  
  printf("end %s\n", (has_argument ? "with argument" : "without argument"));
  return 0;
}

