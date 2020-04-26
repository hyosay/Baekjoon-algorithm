import sys
n = num = int(input())
count = 0
while True:
    A = n // 10
    B = n % 10
    total = A + B
    count += 1
    n = ((n % 10) * 10 + (total % 10))
    if(num == n):
        break
print(count)