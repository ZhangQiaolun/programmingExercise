# Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order
print("Input what you like")
arr_str = input().split(' ')
arr = [int(num) for num in arr_str]
print(arr)
length = len(arr)

for j in range(1, length):
    key = arr[j]
    i = j - 1
    while i >= 0 & arr[i] < key:
        arr[i+1] = arr[i]
        i = i - 1
    arr[i+1] = key
print(arr)

