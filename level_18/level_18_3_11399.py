# N 값을 입력
N = int(input())
# 사람마다 소유 시간을 입력 후 오름차순으로 정렬
people = sorted(list(map(int, input().split())))
time = 0
# 개인 소유 시간을 축적하여 더함
for i in range(0, N):
    if len(people) == N: # N 과 people의 길이가 같은지 확인
        time += sum(people[0:i + 1]) # 합
# 결과
print(time)


# 숏코딩
print(sum(sum(people[:i + 1]) for i in range(N)))
