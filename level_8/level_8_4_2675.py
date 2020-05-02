n = int(input())
S = []
for _ in range(n):
    a,b = input().split()
    output = ""
    for j in b:
        output += j * int(a)
    print(output)


