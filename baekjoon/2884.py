H, N = map(int, input().split())

n_minus = N - 45
h_minus = H
if n_minus < 0:
    n_minus = N - 45 + 60
    if H == 0:
        h_minus = H - 1 + 24
    else:
        h_minus = H - 1


print(h_minus, n_minus)



