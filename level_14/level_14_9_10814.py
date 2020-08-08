N = int(input())
member_list = []
member_list_1= []
for i in range(N):
    member_list.append(input().split())
    member_list_1.append((int(member_list[i][0]), member_list[i][1]))

## 여기서 부터
for i in range(0, N):
    for j in range(0, N - 1):
        if member_list_1[j][0] < member_list_1[j + 1][0]:
            member_list_1[j][0], member_list_1[j + 1][0] = member_list_1[j + 1][0],member_list_1[j][0]
            print(member_list_1)