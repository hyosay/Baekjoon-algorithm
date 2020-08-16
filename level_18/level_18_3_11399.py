N = int(input())
people = sorted(list(map(int, input().split())))

time = 0
for i in people:
    time += i + time
print(time)