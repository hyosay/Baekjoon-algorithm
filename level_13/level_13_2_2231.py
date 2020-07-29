N = int(input())
answer = 0

for i in range(1, N + 1):
    coef_N_list = list(map(int, str(i)))
    answer = i + sum(coef_N_list)

    if answer == N:
        print(i)
        break

    if i == N:
        print(0)