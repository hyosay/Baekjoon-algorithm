KG = int(input())

box = 0

while True:
    if(KG % 5) == 0:
        box = box + (KG // 5)
        print(box)
        break
    KG = KG - 3
    box += 1
    if KG < 0:
        print("-1")
        break