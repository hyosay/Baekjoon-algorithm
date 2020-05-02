import math
a = list(range(0,101))
def slove(a):
    summ = 0
    for i in a:
        summ += i
    return print(summ)


#2
b = math.fsum(a)
print(b)