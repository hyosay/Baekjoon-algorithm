import random
import colorsys
colorsys
def random_number_machine():
    random_number = []
    random_set = []
    for i in range(0, 7):
        random_number.append(random.randint(1, 46))
    random_set = set(random_number)

    while len(random_set) != 7:
        for j in range(0, 7):
            random_number[j] = random.randint(1, 46)
        random_set = set(random_number)
        if len(random_set) == 7:
            break
    for z in range(0, 7):
        out = print(random_number[z], end = ' ')
    return out





my_number = list(map(int, input().split()))

for k in range(1, 6):
    print(k,'회차 :',end = ' ')
    random_number_machine()
    print()







