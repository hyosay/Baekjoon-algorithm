nums = list(map(int, input()))



a = sorted(nums, reverse= True)
for i in a:
    print(i, end= "")