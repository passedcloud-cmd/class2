# ------------------------------------------------------------
# 01. 후위 표기법 수식 계산
# ------------------------------------------------------------
# [중위 표기법] 연산자를 피연산자 '가운데' 표기      2 + 3,  (2 + 3) * 4
# [후위 표기법] 연산자를 피연산자 '뒤에' 표기        23+,    23+4*
#
# [왜 후위 표기법인가]
#   사람에게는 (3 + 5) * 2 가 익숙하지만, 컴퓨터는 이 식을 보면 물어볼 게 많다.
#     "괄호가 있네? 안쪽부터 계산해야 하나?"
#     "+ 와 * 가 있네? 곱하기를 먼저 해야 하나?"
#   후위 표기법은 이 고민을 전부 없앤다. 왼쪽부터 한 번만 읽으면서
#   "숫자는 넣고, 연산자는 꺼내서 계산한다" 규칙 하나로 끝난다.
#
# [비유] 요리 레시피
#   중위 표기법 = "설탕을 넣되, 그 전에 밀가루와 계란을 먼저 섞고..."  (앞뒤를 오가야 함)
#   후위 표기법 = "밀가루, 계란, 섞기, 설탕, 섞기"                     (위에서 아래로 그냥 따라가면 됨)
#
# [학습 목표] 여기서 스택은 '피연산자(숫자) 보관소' 다.
#        02번에서 배울 변환에서는 스택이 '연산자 보관소' 로 역할이 바뀐다.
#        이 둘을 헷갈리지 않는 것이 이 단원의 최대 관문이다.
# ------------------------------------------------------------

# [알고리즘]
#   1. 후위 표기법 식을 왼쪽부터 순회한다.
#   2. 피연산자(숫자)를 만나면 스택에 push
#   3. 연산자를 만나면
#        3-1. 스택에서 피연산자 두 개를 pop
#             ** 먼저 꺼낸 것이 '오른쪽' 피연산자다 **
#        3-2. 연산 결과를 다시 스택에 push
#   4. 식이 끝나면 스택에 하나 남은 값이 정답


def evaluate_postfix(expression):
    stack = []

    for token in expression:
        # 1. 피연산자(숫자)인 경우: 스택에 push
        if token.isdigit():
            # TODO 1) 문자로 된 숫자를 정수로 바꿔서 스택에 넣으세요.
            #   힌트: '2' 와 2 는 다르다. int() 변환을 빼먹으면
            #         '2' + '3' 이 5가 아니라 '23' 이 된다.
            stack.append(int(token))

        # 2. 연산자인 경우: 스택에서 2개 꺼내서 계산
        else:
            # TODO 2) 스택에서 두 개의 숫자를 꺼내세요.
            #   [중요] 스택은 LIFO 이므로, '먼저 꺼낸 것' 이 오른쪽 피연산자다.
            #          순서를 바꾸면 뺄셈과 나눗셈이 틀린다. (아래 함정 확인 참고)
            right = stack.pop()
            left = stack.pop()

            # TODO 3) 연산자에 맞춰 계산하고, 결과를 다시 스택에 넣으세요.
            #   힌트: 나눗셈은 int(left / right) 로 정수 결과를 만든다.
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(left / right)

    # TODO 4) 스택에 남은 마지막 값을 반환하세요.
    return stack.pop()


# --- 실행 테스트 ---
print('=== 후위 표기법 계산 ===')

postfix = '23+4*'  # (2+3)*4 = 20
print(f'  식: {postfix} | 결과: {evaluate_postfix(postfix)}')

postfix2 = '53*2+'  # 5*3+2 = 17
print(f'  식: {postfix2} | 결과: {evaluate_postfix(postfix2)}')

postfix3 = '92-3/'  # (9-2)/3 = 2
print(f'  식: {postfix3} | 결과: {evaluate_postfix(postfix3)}')


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] 토큰 하나마다 스택이 어떻게 변하는지 보기
# ------------------------------------------------------------
def trace_postfix(expression):
    """계산 과정을 단계별로 출력"""
    stack = []
    print(f'  후위 표기식: {expression}')
    print(f'  {"단계":<4} {"토큰":<4} {"동작":<32} {"스택"}')
    print(f'  {"-" * 4} {"-" * 4} {"-" * 32} {"-" * 16}')

    for step, token in enumerate(expression, start=1):
        if token.isdigit():
            stack.append(int(token))
            action = '숫자 -> push'
        else:
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                value = left + right
            elif token == '-':
                value = left - right
            elif token == '*':
                value = left * right
            else:
                value = int(left / right)

            stack.append(value)
            action = f'pop {right}, pop {left} -> {left} {token} {right} = {value}'

        print(f'  {step:<4} {token:<4} {action:<32} {stack}')

    print(f'\n  최종 결과: {stack[-1]}')


print('=== 계산 과정 추적 ===')
trace_postfix('23+4*')

print()
print('=== 순서가 중요한 이유 (뺄셈) ===')
trace_postfix('92-')
# 9 - 2 = 7 이 되어야 한다. 만약 left 와 right 를 바꾸면 2 - 9 = -7 이 나온다.


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [함정 확인] pop 순서를 바꾸면 어떻게 될까?
# ------------------------------------------------------------
def evaluate_wrong(expression):
    """일부러 left / right 를 뒤바꾼 잘못된 버전"""
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            left = stack.pop()  # 잘못된 순서!
            right = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))
    return stack.pop()


print('=== 올바른 순서 vs 뒤바뀐 순서 ===')
print(f'  {"후위식":<7} | {"의미":<8} | {"정답":>4} | {"뒤바뀜":>4}')
print(f'  {"-" * 10} | {"-" * 10} | {"-" * 6} | {"-" * 6}')
for expr, meaning in [('92-', '9 - 2'), ('82/', '8 / 2'), ('23+', '2 + 3'), ('34*', '3 * 4')]:
    mine = evaluate_postfix(expr)
    print(f'  {expr:<10} | {meaning:<10} | {mine!s:>6} | {evaluate_wrong(expr):>6}')


# [포인트] + 와 * 는 순서를 바꿔도 답이 같아서 실수를 눈치채지 못한다.
#          - 와 / 에서만 틀리기 때문에, 테스트를 + 로만 하면 버그를 놓친다.
#          => 테스트 케이스는 반드시 뺄셈/나눗셈을 포함시킬 것.


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [스스로 점검하기]
# ------------------------------------------------------------
# Q1. right 와 left 를 뒤바꾸면 왜 '+' 와 '*' 에서는 티가 안 날까?
#     테스트를 '23+' 로만 하면 버그를 놓치는 이유를 설명해 보자.
#
# Q2. stack.pop() - stack.pop() 이라고 한 줄로 쓰면 어떤 순서로 계산될까?
#
# Q3. int(token) 변환을 빼먹으면 '23+' 의 결과는 무엇이 될까? 직접 지워서 확인해 보자.
#
# Q4. '12 3 +' 처럼 두 자리 숫자가 있는 식은 왜 이 코드로 처리되지 않을까?
#     (해결책은 03번 파일에서 다룬다)
#
# Q5. 마지막에 stack.pop() 대신 stack 을 반환하면 무엇이 달라질까?
