import math
a = list(range(0,101))

def slove(a):
    sum = 0
    for i in a:
        sum += i
    return print(sum)


#2
b = math.fsum(a)
print(b)