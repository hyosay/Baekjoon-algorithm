A = set(range(1,10001))
B = set()

for i in range(1,10001):#22
    for j in str(i):
        i += int(j)
    B.add(i)

C = A - B
C = sorted(C)
for k in C:
    print(k)
