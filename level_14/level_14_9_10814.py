import sys
N = int(sys.stdin.readline())
member_list = []
member_list_1= []
for i in range(N):
    member_list.append(sys.stdin.readline().split())
    member_list_1.append((int(member_list[i][0]), member_list[i][1]))


member_list_1 = sorted(member_list_1, key= lambda x: x[0])
for i, j in member_list_1:
    print(i, j)