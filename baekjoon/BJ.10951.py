#풀이1
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

# 풀이2
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
# 풀이3
try:
    while 1:
        a, b = map(int, input().split())
        print(a+b)
except:
    exit()

# 풀이4
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

