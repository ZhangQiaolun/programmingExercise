// 该版本可以处理double类型
#include <stdio.h>
#include <math.h>

void printOut(int number);
void printDigit(int number);
void preDispose(int number);

int main(void)
{
	double n = 9.1;
	
	preDispose(n);
	
	return 0;
}

// 函数modf把传入的第一个参数分为整数和小数两部分，整数部分保存在
// 第二个参数中，两部分的正负号均匀x相同，函数返回小数部分
double fraction = modf(number, &ip);
