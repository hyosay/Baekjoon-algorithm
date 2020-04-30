case = int(input())
for i in range(case):
    average = 0
    count = 0
    A = list(map(int, input().split()))
    for k in range(1, len(A)):
        average = average + A[k]
    standard = average / A[0]
    for j in range(1,len(A)):
        if A[j] > standard:
            count = count + 1
        else:
            count = count + 0
    print('%.3f' % (count / A[0] * 100) + '%')
