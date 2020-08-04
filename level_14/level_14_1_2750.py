N = int(input())
array = []
for i in range(0, N):   array.append(int(input()))
print(array)
'''
for i in range(0, N):
    for j in range(0, N):
        if array[i] < array[j]:
            array[j], array[i] = array[i], array[j]
print(array)




#bubble sort
for i in range(0, N):
    for j in range(0, N - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print(array)


# selection sort
for i in range(0, N):
    min = 1000
    for j in range(i, N):
        if min > array[j]:
            min = array[j]
            index = j
    temp = array[i]
    array[i] = min
    array[index] = temp

for k in range(0, N):
    print(array[k])'''


#insertion sort
for i in range(0, N - 1):
    j = i
    while array[j] > array[j + 1]:
        array[j + 1], array[j] = array[j], array[j + 1]
        if j > 0:
            j = j - 1
print(array)