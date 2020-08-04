N = int(input())
a = [int(input()) for i in range(0, N)]
def Quicksort(data, start, end):
    if start >= end:
        return

    pivot = start
    L = start
    R = end

    while L < R:
        while data[L] < data[pivot]:
            L = L + 1
        while data[R] > data[pivot] and R > start:
            R = R - 1

        if L > R:
            data[L], data[R] = data[R], data[L]
        else:
            data[R], data[pivot] = data[pivot], data[R]

    Quicksort(data, start, R - 1)
    Quicksort(data,L + 1, end)

Quicksort(a, 0, N - 1)
for i in range(0, N):
    print(a[i])

