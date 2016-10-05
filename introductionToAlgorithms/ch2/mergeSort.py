def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    left = A[p:q]
    right = A[q:r+1]
    lenL = q - p
    lenR = r + 1 - q
    for i in range(lenL):
        left[i] = A[p+i]
    for j in range(lenR):
        right[j] = A[q+j]

    i = 0
    j = 0
    for k in range(r-p+1):
        if left[i] < right[j]:
            A[p+k] = left[i]
            i = i + 1
        else:
            A[p+k] = right[j]
            j = j + 1
        if i == (q-p):
            break
        if j == (r+1-q + 1):
            break
    if i == (lenL):
        for m in range(lenR-j+1):
            A[k+m+1] = right[j+m]
    if j == lenR:
        for n in range(lenL-i+1):
            A[k+n+1] = left[i+n]
A = [3, 4, 0, 1, 5]
mergeSort(A, 0,  4)
print(A)
