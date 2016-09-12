#include <stdio.h>

void printOut(int number);
void printDigit(int number);
void preDispose(int number);

int main(void)
{
	int n = -45689;
	
	preDispose(n);
	return 0;
}

void preDispose(int number)
{
	if(number < 0) {
		putchar('-');
		number = -number;
	}
	
	printOut(number);
}

void printOut(int number)
{
	int value = number / 10;
	
	if(value != 0)
		printOut(value);
	
	printDigit(number % 10);
}

void printDigit(int number)
{
	printf("%d", number);
}