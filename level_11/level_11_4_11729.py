'''def hanoi(N, start, target, middle):
    if N == 1:
        print(start, target)
        return
    hanoi(N - 1, start, middle, target)

    print(start, target)

    hanoi(N - 1, middle, target, start)

def hanoi_count(N):
    count = pow(2, N) -1
    return print(count)


N = int(input())
hanoi_count(N)
hanoi(N,1,3,2)'''

def h(n, a, b, c):
    if n == 1:print(a, c);return
    h(n-1,a, c, b);print(a, c);h(n-1,b,a,c)
k = int(input())
print(2 ** k - 1)
h(k,1,2,3)