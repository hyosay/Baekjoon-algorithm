#10825



N = int(input())
student = []

#람다식을 활용하여 문제를 해결
# 오름차순과 내림차순을 변경할떄 - 부호를 넣어준다.
'''
for _ in range(N):
    student.append(input().split())
student = sorted(student, key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(0, N):
    print(student[i][0])
'''

# 람다식을 사용하지 않고 sort를 이용
# 조건을 전부 100 - (내림차순) 으로 해서 오름차순으로 바꿈

student1 = []
for _ in range(N):
    name, a, b, c = map(str,input().split())
    student1.append([100 - int(a), int(b), 100 - int(c), name])
student1.sort()
for i in student1:
    print(i[-1])


