row , column = map(int, input().split())
BW = []
for i in range(0, row):
    BW.append([i for i in input()])

for i in range(0, row):
    for j in range(i, column):
        if BW[i][j] == BW[i][j]:
            BW[i][j] == 'W'

print(BW)

