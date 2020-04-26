N = int(input()) #N * 2

for i in range(0, N * 2):
    if N <= 3:
        if i % 2 == 0:
            print(('*' + ' ') * round(N / 2))
        else:
            print((' ' + '*') * (round(N / 2)))
    else:
        if i  % 2 == 0:
            print(('*' + ' ') * round(N / 2))
        else:
            print((' ' + '*') * (round(N / 2)))


