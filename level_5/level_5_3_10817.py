#1
A ,B ,C = map(int,input().split())
if A <= B and B <= C:
    print(B)
elif A <= C and C <= B:
    print(C)
elif B <= A and A <= C:
    print(A)
elif B <= C and C <= A:
    print(C)
elif C <= A and A <= B:
    print(A)
elif C <= B and B <= A:
    print(B)


#2
data = list(input().split())


for i in range(len(data)):
    data[i] = int(data[i])

sorted_list = sorted(data, reverse = True)
#or
sorted_list = sorted(data)

print(sorted_list[1])