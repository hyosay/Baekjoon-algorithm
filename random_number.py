import random

#로또 번호 생성
random_number = []

sr = []

while len(sr) < 7:
    for i in range(0, 7):
        random_number.append(random.randint(1, 46))
    sr = set(random_number)
    if len(sr) == 7:
        break


#중복 되는 수 제거

print("로또 넘버 :", random_number[0],random_number[1], random_number[2], random_number[3], random_number[4], random_number[5])
print("보너스 넘버 :", random_number[6])

#내가 선택한 로또 번호
print("당신의 넘버를 입력하시요.")

coice_number = list(map(int, input().split()))

# 로또 번호 비교
count = []
for i in range(0, 7):
    for j in range(0,7):
        if random_number[i] == coice_number[j]:
            count.append(coice_number[j])
print(len(set(count)))