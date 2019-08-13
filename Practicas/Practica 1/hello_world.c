#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	int var = atoi(argv[1]);
	int ran;

	for (int i = 1; i <= var; i++) {
		ran = (rand()%6)+1;
		printf("\033[1;3%im",ran);
		printf("#%i: FSE2020-1 Marco Moreno\n",i);
	}

	return 0;
}
