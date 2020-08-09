N = int(input())
answer = 0

for i in range(1, N + 1):
    coef_N_list = list(map(int, str(i)))
    print(coef_N_list)
    answer = i + sum(coef_N_list)
    print(answer)

    if answer == N:
        print(i)
        break

    if i == N:
        print(0)
