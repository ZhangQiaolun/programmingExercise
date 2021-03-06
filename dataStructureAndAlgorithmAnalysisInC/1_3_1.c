#include <stdio.h>

void printOut(int number);
void printDigit(int number);

int main(void)
{
	int n = 123;
	printOut(n);
	
	return 0;
}

void printOut(int number)
{
	int value = number / 10;
	
	// 考虑用while会出现什么情况，如果数字不是个位数，那么就会死循环
	// 因为在while里头value一直没有变，printOut（value）会一直干下去
	if (value != 0)
		printOut(value);
	
	printDigit(number % 10);
}

void printDigit(int number)
{
	printf("%d", number);
}