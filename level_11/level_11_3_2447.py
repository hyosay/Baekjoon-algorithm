def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum
print(solve([a for a in range(0,11) if a % 2== 0]))
