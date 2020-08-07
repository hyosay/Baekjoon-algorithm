import sys
N = int(sys.stdin.readline())
xy = [list(map(int, sys.stdin.readline().split())) for xy in range(0, N)]
'''
for i in range(N):
    min = 999
    for j in range(i, N):
        if min > xy[j][1]:
            min = xy[j][1]
            xy[i],xy[j] = xy[j], xy[i]
for i in range(N):
    print(xy[i][0], xy[i][1])'''
xy = sorted(xy, key= lambda)
