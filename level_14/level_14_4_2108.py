
N = int(input())
N = [int(input()) for i in range(0, N)]
def n1(N):
    return sum(N) / len(N)
def n2(N):
    sor = sorted(N, reverse= False)
    midd = int((len(N) / 2))
    return sor[midd]
def n3(N):
    mx = max(N)
    array = [0] * mx
    for i in N:
        array[i - 1] += 1
    if array.index(max(array)) == 0:
        return 1
    else:
        return array.index(max(array))


print(n3(N))







