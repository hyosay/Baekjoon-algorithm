# 10825
N = int(input())

student = []

for i in range(N):
    student.append((input().split(" ")))
    while student[i][0] == type(str):
        print(student[i][0])


