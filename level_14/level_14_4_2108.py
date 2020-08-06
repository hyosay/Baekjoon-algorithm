import sys
N = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for i in range(0, N)]
def n1(N):
    return round(sum(N) / len(N))
def n2(N):
    sor = sorted(N, reverse= False)
    midd = int((len(N) / 2))
    return sor[midd]
def n3(N):

    for i in N:
        if i < 0:
            mi = [0] * (max(N) + abs(min(N)) + 1)
            break
        else:
            mi = [0] * (max(N) + 1)

    kill = len(mi) - max(N) - 1
    for i in N:
        if i > 0:
            mi[i + kill] += 1
        else:
            mi[i + kill] += 1

    maxmi = max(mi)
    temp = maxmi
    a = []
    #이 부분 다시 설정
    for k in range(-kill, len(mi) - kill):
        if temp <= mi[k + kill]:
            temp = mi[k + kill]
            a.append(k)
    print(mi)
    if len(a) <= 2:
        return a[0]
    else:
        return a[1]

def n4(N):
    return max(N) - min(N)

print(n1(N))
print(n2(N))
print(n3(N))
print(n4(N))


