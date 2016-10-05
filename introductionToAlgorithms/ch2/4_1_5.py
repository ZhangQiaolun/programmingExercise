# 为最大子数组问题设计一个非递归的，线性时间的算法
# 基于如下性质求A[1..j+1]的最大字数组，A[1..j+1]的最大字数组要么是A[1..j]的最大字数组，要么是某个字数组A[i..j+1]。
# 在已知A[1..j]的最大子数组的情况下，可以在线性时间内找出形如A[i..j+1]的最大字数组
numbers = [1, -2, 3, 9, -5, 6]
maxValue = numbers[0]
headIndex = tailIndex = 0

def getmaxAfter(i):


def getmaxSubArray(headIndex, tailIndex, maxValue, i):
    headAfterIndex, tailAfterIndex, maxAfter = getmaxAfter(i)
    if maxAfter >=  maxValue:
        headIndex = headAfterIndex
        tailIndex = tailAfterIndex
        maxValue = maxAfter

for i in range(1, len(numbers)):
    maxAfter = numbers[i]
    for j in range(1, i+1):
        getmaxSubArray(headIndex, tailIndex, maxValue, j)
print(headIndex, tailIndex)
