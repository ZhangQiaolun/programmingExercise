#include <stdio.h>
#include <stdlib.h>

void printDigit(int a) {
    printf("%d", a);
}

void printOut(unsigned int N) {
	if (N >= 10)
		printDigit(N / 10);
	printDigit(N % 10);
}

int main()
{
	printOut(100);
	return 0;
}
