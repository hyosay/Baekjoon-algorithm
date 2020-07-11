"""kg = int(input())

box = 0

while True:
    if (kg % 5) == 0:
        box = box + (kg // 5)
        print(box)
        break
    else:
        kg = kg - 3
        box = box + 1
        if kg < 0:
            print("-1")
            break
"""
n = int(input())
print([n//5 + [0, 2 - n % 5 % 2][n % 5 > 0], -1][n in [4, 7]])
1 6 12  26