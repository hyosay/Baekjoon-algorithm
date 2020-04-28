number_remainder = []
number_count = 0
a = 0
for i in range(10):
    number = int(input())
    number_remainder.append(number % 42)
number_remainder = set(number_remainder)
print(len(number_remainder))