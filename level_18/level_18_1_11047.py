N, K = map(int, input().split())
money = []
for i in range(N):
    money.append(int(input()))
money.sort(reverse= True)
count = 0
for i in money:
    count += K // i
    K %= i
print(count)
