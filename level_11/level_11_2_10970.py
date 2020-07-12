"""N = int(input()) #3
def fa(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fa(N - 1) + fa(N - 2) # 3 + fa(2

print(fa(N))"""

#exec()함수를 통한 파보나치 수
a = 0; b=1
exec("a, b = b, a+ b;" * int(input()))
print(a)

