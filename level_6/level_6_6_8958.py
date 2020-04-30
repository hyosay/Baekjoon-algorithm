count = 0
count1 = 0
a = 0
for i in range(int(input())):
    count1 = 0
    count = 0
    ox = str(input())
    for k in ox:
        if k == 'O':
            count = count + 1
        elif k == 'X':
            count = 0
        count1 = count1 + count
    print(count1)
