import sys
N = int(sys.stdin.readline())
xy = []
for i in range(0, N):
    xy.append(list(map(int, sys.stdin.readline().split())))

xy = sorted(xy, reverse= False)
for j in range(0, N):
    print(xy[j][0], xy[j][1])
