n, m = map(int, input().split())
n_card = input().split()
n_card = list(map(int, n_card))
best = 0
for i in range(0, n):
    sum = 0
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = n_card[i] + n_card[j] + n_card[k]
            if sum <= m:
                best = max(best, sum)
print(best)





