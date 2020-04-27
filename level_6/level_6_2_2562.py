#1
number = []
for i in range(0, 9):
    number.append(int(input()))

ma = max(number)
print((ma))
print(number.index(ma) + 1)

#2
max_number = 0
index_number = 0
for i in range(9):
    a = int(input())

    if max_number < a:
        max_number = a
        index_number = i + 1
print(max_number)
print(index_number)
