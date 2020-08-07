array = [-1,-2, -3, -1, -2]

for i in range(0, len(array)):
    if array[i] < 0:
        mi = [0] * (max(array) + abs(min(array)) + 1)
    else:
        mi = [0] * (max(array) + 1) #0 ~  max

kill = len(mi) - max(array) - 1

for i in array:
    if i > 0:
        mi[i + kill] += 1
    else:
        mi[i + kill] += 1

print(mi)

maxmi = max(mi)
temp = maxmi
a = []

for k in range(-kill, len(mi) - kill):
    if temp <= mi[k + kill]:
         temp = mi[k + kill]
         a.append(k)

print(a)
if len(a) <= 2:
    if a[0] < 0:
        print(a[1])
    else:
        print(a[0])
else:
    print(a[1])
for i in a:


