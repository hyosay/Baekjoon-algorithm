#1 my coding
num = input().split()
rev1 = []
for i in num: # 123, 345
    rev_num = list(reversed(i))
    rev1.append(int("".join(rev_num)))
print(max(rev1))

#shot coding
print(max(input()[::-1].split()))

