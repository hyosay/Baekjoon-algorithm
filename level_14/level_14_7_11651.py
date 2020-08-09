'''N = int(input())
xy = [list(map(int, input().split())) for xy in range(0, N)]
xy = sorted(xy, key= lambda x: x[-1], reverse= False)
for i in range(0, N):
    print(xy[i][0], xy[i][1])

'''
import sys
n = int(sys.stdin.readline())
xy  = []
for i in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))
xy.sort(key= lambda x: (x[1],x[0]))
for i in xy:
    print(i[0],i[1])