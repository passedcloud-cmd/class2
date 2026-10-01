import sys
sys.stdin = open("01_후위표기법.txt")
T = int(input())
for test_case in range(1, T + 1):
    # 문자열 받아오기
    text_calculation = input()

    # 연산자를 push할 stack 리스트
    stack = []
    # 결과 출력을 push할 result 리스트
    result = []

    for token in text_calculation:
        # 토큰이 숫자면 result에 push
        if token.isdigit():
            result.append(token)

        # 토큰이 숫자가 아니면(=연산자면) stack에 push
        else:
            stack.append(token)

    # stack이 비어질 때까지 stack에 있는 값들을 pop 해서 result에 넣기
    while stack:
        result.append(stack.pop())

    # result 리스트에 있는 값들을 하나로 이어서 출력
    print(f'{test_case} {"".join(result)}')










    #
    # # 연산자 우선순위
    # precedence = {
    #     '+': 1,
    #     '-': 1,
    #     '*': 2,
    #     '/': 2,
    #     '(': 0,
    # }
    #
    # # 연산자 저장 용 스택 만들기
    # stack = []
    # # 결과를 담을 리스트
    # result = []
    #
    # for token in text_calculation:
    #     # 숫자면 결과에 추가
    #     if token.isdigit():
    #         result.append(token)
    #
    #     # (면 stack에 push
    #     elif token == '(':
    #         stack.append(token)
    #
    #     # )면 여는 괄호가 나올 때까지 stack에서 pop을 하고 result에 추가
    #     elif token == ')':
    #         # stack이 비지 않고 마지막 값이 (가 아니라면 반복
    #         while len(stack) != 0 and stack[-1] != '(':
    #             result.append(stack.pop())
    #         # stack에서 (를 발견하면 while문 탈출 후 (제거
    #         stack.pop()
    #
    #     # +, - , *, / 연산자 우선순위 비교
    #     else:
    #         #stack이 비어있지 않고, stack의 맨 위에 있는 것과 현재 token의 우선순위 비교
    #         while stack and precedence[stack[-1]] >= precedence[token]:
    #             result.append(stack.pop())
    #
    #         # 우선순위가 높거나 같은 것들을 stack에서 내보낸 뒤 현재 token을 stack에 push
    #         stack.append(token)
    #
    # # stack에 남은 것들을 전부 pop으로 result에 넣기
    # while stack:
    #     result.append(stack.pop())
    #
    # sum_text = "".join(result)
    # print(f'#{test_case} {sum_text}')






# 입력
# 3
# 2+3*4/5
# 1*2/3+2
# 3-2*5+4/2-2
#
# 출력
# #1 2345/*+
# #2 1232+/*
# #3 325422-/+*-