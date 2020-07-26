N = int(input())

array = []
for i in range(0, N):
    array.append(int(input()))

for i in range(0, N):
    array.sort(reverse= False)
    print(array[i])