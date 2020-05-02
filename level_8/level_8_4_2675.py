n = int(input())
a = []
for _ in range(n):
    a,b = input().split()
    output = ""
    for j in b:
        output += j * int(a)
    print(output)