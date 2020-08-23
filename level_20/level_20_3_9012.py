# N을 입력
N = int(input())
# 문자열을 담을 리스트 자료형 초기화
stack = []
# 괄호 문자열 입력
for i in range(N):
    stack.append(input())
# 반복
for i in range(N):
    # 횟수 초기화
    count = 0
    for j in range(len(stack[i])):
        # '(' 이면 +1을 ')'이면 -1을 count 입력
        if stack[i][j] == '(':
            count += 1
        else:
            count -= 1
        # ')'가 먼저 시작되거나 '('보다 ')'가 많을시 break
        if count < 0:
            break
    # count가 0이면 YES를 출력
    if count == 0:
        print("YES")
    # count가 -1이거나 0보다 높으면 NO를 출력
    else:
        print("NO")

