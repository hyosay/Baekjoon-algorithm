number_remainder = []
number_count = 0
for i in range(10):
    number = int(input())
    number_remainder.append(number % 42)
list_remainder = str(number_remainder)
for j in list_remainder:
    number_count = number_count + number_remainder.count(str(j))
print(number_count)