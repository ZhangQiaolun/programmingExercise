#!/usr/bin/env python
#coding:utf-8

# 方法1

def quickSort(arr):
    less = []
    pivotlist = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less + pivotList + more

# 方法2
def quickSort2(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        # 边界点的加1减1不能忘掉
        quickSort2(arr, p, q-1)
        quickSort2(arr, q+1, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

arr = [9, 3, 8, 1]
quickSort2(arr, 0, 3)
print(arr)
