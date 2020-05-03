dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
count = 0
for i in range(len(a)):
    for j in dial:
        if i == dial[j]:
            count += 1
print(count)

