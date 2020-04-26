#1
N = int(input())
A = -1
B = N - 1
for i in range(N,0,-1):
    A = A + 1
    dot = ' ' * A
    star = '*' * (i * 2 - 1)
    print(dot + star)
for j in range(2,N + 1):
    B = B - 1
    dot = ' ' * B
    star = '*' * (j * 2 - 1)
    print(dot + star)
#2
a = int(input())
b = a
for i in range(1, a + 1):
    print(' ' * (i - 1) + '*' * (2*(b - i) + 1))
for j in range(1, b):
    print(' ' * (b - j - 1) + '*' * (2 * j + 1))