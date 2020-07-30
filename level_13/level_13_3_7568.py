wight = []
ki = []
student = []
N = int(input())
for i in range(0, N):
    a,b = list(map(int, input().split()))
    student.append((a, b))


for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
