import sys
sys.stdin = open("4874-Forth.txt")
T = int(input())
for test_case in range(1, T + 1):
    text_calculation = input().split()

    # 연산자를 넣을 stack
    stack = []

    for token in text_calculation:
        # 숫자면 stack에 push
        if token.isdigit():
            stack.append(int(token))

        # 연산자면 스택에서 숫자 2개를 꺼내서 계산
        elif token == "+" or token == "-" or token == "*" or token == "/":
            # stack에서 위에 있는 값이 오른쪽
            if stack:
                right = stack.pop()
            # 만약 stack에 값이 없으면 error 출력
            else:
                result = "error"
                break # for token

            if stack:
                left = stack.pop()
            else:
                result = "error"
                break # for token

            # 연산자 4개 계산 결과를 stack에 추가
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left / right)
        # 만약 "."이라면 스택에서 숫자를 꺼내 출력
        elif token == ".":
            result = round(stack.pop())

    # stack에 값이 있으면 오류
    if stack:
        result = 'error'

    print(f'#{test_case} {result}')


#
# 출력
# #1 84
# #2 error
# #3 168
# #4 error
# #5 5
# #6 2
# #7 336
# #8 error
# #9 14028
# #10 84
# #11 42