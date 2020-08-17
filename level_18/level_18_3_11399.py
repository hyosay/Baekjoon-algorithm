N = int(input())
people = sorted(list(map(int, input().split())))
time = 0
for i in range(0, N):
    if len(people) == N:
        time += sum(people[0:i + 1])
print(time)


# 숏코딩
print(sum(sum(people[:i + 1]) for i in range(N)))
