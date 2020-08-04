import sys

N = int(input())
array = [0] * 10001
for i in range(N):
    input_num = int(sys.stdin.readline())

    array[input_num] = array[input_num] + 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
