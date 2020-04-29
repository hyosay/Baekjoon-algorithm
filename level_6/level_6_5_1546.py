total_len = int(input())
total_point = list(map(float, input().split()))
M = max(total_point)
Average = 0
for i in total_point:
    Average = Average + (i / M * 100)
total_score = Average / total_len
print(total_score)
