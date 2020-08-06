import math
math
array = [1,3,8, 2, -2]
mi = [0] * (max(array) + 1) #0 ~  max
if min(array) < 0:
    minus = [0] * (abs(min(array)))
print(mi)
print(minus)

'''
for i in array:
    if i > 0:
        mi[i] += 1
        print(mi)


maxmi = max(mi)
temp = maxmi
a = []
for k in range(0, len(mi)):
    if temp <= mi[k]:
         temp = mi[k]
         a.append(k)
print(a)
if len(a) <= 2:
    print(a[0])
else:
    print(a[1])'''



