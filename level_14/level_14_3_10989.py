#카운팅 정렬
import sys
N = int(sys.stdin.readline())
array = []
count = [0] * N
for i in range(0, N):
    array.append(int(sys.stdin.readline()))
for i in range(0, N):
    count[array[i] - 1] += 1
for i in range(0, len(count)):
    if count[i] != 0:
        for j in range(0, count[i]):
            print(i + 1)