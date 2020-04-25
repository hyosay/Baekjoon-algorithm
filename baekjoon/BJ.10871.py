N, X = map(int,input().split())


A = list(map(int,input().split()))

for i in range(0,N):
    if X > A[i]:
        print(A[i],end=' ')



