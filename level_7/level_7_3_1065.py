a = int(input())
count = 0
for i in range(1, a + 1):
    if i <= 99:
        count += 1
    else:
        ab = list(map(int, str(i)))
        if ab[0] - ab[1] == ab[1] - ab[2]:# 등차수열 공식
            count += 1
print(count)