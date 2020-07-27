#카운팅 정렬


array = [1, 9, 3, 3, 2, 1, 6, 5, 4, 4]
array_count = [0] * 11
array_sum = [0] * 11
N = len(array)
'''for i in range(0, N):
    array.append(int(input()))'''
for i in range(0, N):
    array_count[array[i]] += 1
print(array_count)

array_sum[0] = array_count[0]
for i in range(1, 12):
    array_sum[i] = array_sum[i - 1] + array_count[i]
print(array_sum)