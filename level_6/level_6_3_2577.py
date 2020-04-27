A = int(input())
B = int(input())
C = int(input())

ABC = A * B * C
list_ABC = list(str(ABC))
for i in range(10):
    list_count = list_ABC.count(str(i))
    print(list_count)