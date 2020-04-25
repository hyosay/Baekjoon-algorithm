T = int(input()) + 1
for i in range(1, T):
    a,b = map(int, input().split())
    print("Case #"+ str(i) +':',a, "+", b,'=', a + b)