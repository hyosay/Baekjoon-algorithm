row , column = map(int, input().split())
BW = []
for i in range(0, row):
    BW.append([i for i in input()])
bc = 0
wc = 0
for i in range(row):
    for j in range(column):
        if BW[i][j] == "B":
            bc += 1
        elif BW[i][j] == "W":
            wc += 1
print(bc, wc)
