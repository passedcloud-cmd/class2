# ------------------------------------------------------------
# 02. 중위 표기법 -> 후위 표기법 변환
# ------------------------------------------------------------
# 01번에서 후위 표기법이 계산하기 얼마나 편한지 확인했다.
# 그렇다면 사람이 쓰는 중위 표기법을 그 편한 형태로 어떻게 바꿀까?
#
# [학습 목표] 스택의 역할이 01번과 정반대다.
#          01번 (계산) : 스택 = 피연산자(숫자) 보관소, 결과물은 숫자
#          02번 (변환) : 스택 = 연산자 보관소,        결과물은 문자열
#        "피연산자는 순서가 안 바뀌고, 연산자만 순서가 바뀐다"
#        => 그래서 순서를 미뤄야 하는 연산자만 스택에 잠시 보관하는 것이다.
#
# [비유] 대기실
#   숫자는 도착하는 대로 바로 무대(결과)로 나간다.
#   연산자는 "나보다 급한 애가 아직 남았나?" 확인하고 대기실(스택)에서 기다린다.
#   나보다 우선순위가 높거나 같은 선배가 대기실에 있으면, 그 선배부터 내보낸다.
# ------------------------------------------------------------

# [알고리즘]
#   1. 중위 표현식을 왼쪽부터 한 글자씩 읽는다.
#   2. 피연산자(숫자, 문자)는 바로 결과에 추가한다.
#   3. 여는 괄호 '(' 는 무조건 스택에 push
#   4. 닫는 괄호 ')' 는 여는 괄호를 만나기 전까지 pop 하여 결과에 추가
#        단, 여는 괄호 '(' 도 pop 하되 결과에는 넣지 않는다.
#   5. 연산자는 스택 top 과 우선순위를 비교한다.
#        - 스택 top 의 우선순위가 나보다 높거나 같으면 -> pop 하여 결과에 추가
#        - 그렇지 않으면 -> 스택에 push
#   6. 모든 토큰을 처리한 뒤, 스택에 남은 연산자를 전부 pop 하여 결과에 추가


def infix_to_postfix(expression):
    # 1. 연산자 우선순위 사전 (숫자가 클수록 높음)
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,  # 스택 '안'에 있을 때는 가장 낮게 -> 아무도 '(' 를 밀어내지 못한다
    }

    stack = []  # 연산자를 저장할 스택
    result = []  # 결과를 담을 리스트

    for token in expression:
        # 1. 피연산자(숫자/문자)인 경우: 바로 결과에 추가
        if token.isalnum():
            # TODO 1) 피연산자는 순서가 바뀌지 않는다. 결과에 바로 담으세요.
            result.append(token)

        # 2. 여는 괄호 '(': 무조건 스택에 push
        elif token == '(':
            # TODO 2) 여는 괄호는 우선순위 비교 없이 무조건 스택에 넣습니다.
            stack.append(token)

        # 3. 닫는 괄호 ')': 여는 괄호가 나올 때까지 pop & 결과에 추가
        elif token == ')':
            # TODO 3) 스택이 비어있지 않고 top 이 '(' 가 아닌 동안 반복하며
            #         pop 한 연산자를 결과에 담으세요.
            #   힌트: while stack and stack[-1] != '(':
            while len(stack) != 0 and stack[-1] != '(':
                result.append(stack.pop())
            # while stack and stack[-1] != '(': 라고 해도 됨
            # TODO 4) 반복이 끝나면 스택 top 에 '(' 가 남아 있다.
            #         이것도 꺼내되 결과에는 담지 않습니다.
            stack.pop()  # 남아있는 '('를 제거해야 하기 때문. '('는 출력에 포함되지 않음.

        # 4. 연산자 (+, -, *, /): 우선순위 비교
        else:
            # TODO 5) 스택 top 의 우선순위가 현재 연산자보다 '높거나 같으면'
            #         pop 해서 결과에 담으세요.
            #   힌트: while stack and precedence[stack[-1]] >= precedence[token]:
            #   [주의] > 가 아니라 >= 다. 같은 우선순위끼리는 왼쪽부터 계산해야 하므로.
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())

            # TODO 6) 비교가 끝난 뒤 현재 연산자를 스택에 넣으세요.
            stack.append(token) # 나보다 높은 애들 다 결과로 보내고 난 뒤에 push

    # TODO 7) 모든 토큰을 처리한 후, 스택에 남은 연산자를 전부 pop 해서 결과에 담으세요.
    #   힌트: while stack:
    while stack:
        result.append(stack.pop())

    # 결과 리스트를 문자열로 변환하여 반환
    return ''.join(result)


# --- 실행 테스트 ---
print('=== 중위 -> 후위 변환 ===')

test_cases = [
    ('(2+3)*4', '23+4*'),
    ('2+3*4-5', '234*+5-'),
    ('2*(3+4)/5', '234+*5/'),
    ('A+B*C', 'ABC*+'),
]

for infix, expected in test_cases:
    actual = infix_to_postfix(infix)
    mark = 'O' if actual == expected else 'X'
    print(f'  중위: {infix:<12} -> 후위: {actual:<10} (기대: {expected:<10}) {mark}')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] 토큰 하나마다 스택과 결과가 어떻게 변하는지 보기
# ------------------------------------------------------------
def trace_conversion(expression):
    """변환 과정을 단계별로 출력"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []

    print(f'  중위 표기식: {expression}')
    print(f'  {"토큰":<4} {"동작":<30} {"스택":<14} {"결과"}')
    print(f'  {"-" * 4} {"-" * 30} {"-" * 14} {"-" * 12}')

    for token in expression:
        if token.isalnum():
            result.append(token)
            action = '피연산자 -> 결과로 바로'

        elif token == '(':
            stack.append(token)
            action = '여는 괄호 -> push'

        elif token == ')':
            popped = []
            while stack and stack[-1] != '(':
                popped.append(stack.pop())
                result.append(popped[-1])
            stack.pop()
            action = f'닫는 괄호 -> {popped} 꺼내고 ( 버림'

        else:
            popped = []
            while stack and precedence[stack[-1]] >= precedence[token]:
                popped.append(stack.pop())
                result.append(popped[-1])
            stack.append(token)
            if popped:
                action = f'연산자 -> {popped} 먼저 내보내고 push'
            else:
                action = '연산자 -> 바로 push'

        print(f'  {token:<4} {action:<30} {stack!s:<14} {"".join(result)}')

    if stack:
        remain = list(reversed(stack))
        result.extend(remain)
        stack.clear()
        print(f'  {"끝":<4} {f"남은 연산자 {remain} 전부 pop":<30} {stack!s:<14} {"".join(result)}')

    print(f'\n  최종 결과: {"".join(result)}')


print('=== 변환 과정 추적 (괄호 있음) ===')
trace_conversion('(2+3)*4')

print()
print('=== 변환 과정 추적 (우선순위 비교) ===')
trace_conversion('2+3*4-5')

# [읽는 법]
#   '2+3*4-5' 에서 '*' 가 들어올 때 스택 top 은 '+' 다.
#   '+'(1) >= '*'(2) 가 거짓이므로 '+' 는 그대로 대기하고 '*' 가 위에 쌓인다.
#   그 다음 '-' 가 들어오면 '*'(2) >= '-'(1) 이 참이라 '*' 가 먼저 나가고,
#   이어서 '+'(1) >= '-'(1) 도 참이라 '+' 도 나간다.
#   => 우선순위가 높은 연산자가 결과 문자열에 먼저 도착한다.


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [연결 확인] 01번에서 만든 계산기로 변환 결과를 검증하기
# ------------------------------------------------------------
def evaluate_postfix(expression):
    """01번 파일의 계산 함수 (검증용)"""
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))
    return stack.pop()


print('=== 변환 -> 계산 -> 파이썬 결과와 대조 ===')
print(f'  {"중위식":<12} | {"후위식":<10} | {"계산":>5} | {"파이썬 eval":>10} | 일치')
print(f'  {"-" * 12} | {"-" * 10} | {"-" * 5} | {"-" * 10} | ----')
for infix in ['(2+3)*4', '2+3*4-5', '2*(3+4)/5', '8/2+1']:
    postfix = infix_to_postfix(infix)

    # 변환기가 아직 미완성이면 계산할 수 없으므로 '-' 로 표시한다
    try:
        mine = evaluate_postfix(postfix)
    except IndexError:
        mine = '-'

    truth = int(eval(infix))  # 검증용으로만 사용 (실습 코드에서는 쓰지 말 것)
    mark = 'O' if mine == truth else 'X'
    print(f'  {infix:<12} | {postfix:<10} | {mine!s:>5} | {truth:>10} | {mark}')

# [포인트] 변환기와 계산기를 이어 붙이면 곧 '계산기 프로그램'이 된다.
#          03번 파일에서 이 둘을 하나로 합친다.


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [스스로 점검하기]
# ------------------------------------------------------------
# Q1. precedence 딕셔너리에서 '(' 를 지우면 어떤 에러가 날까? 직접 지워서 확인해 보자.
#     '(' 를 0으로 두면 어떤 성질이 자동으로 보장될까?
#
# Q2. TODO 5 의 부등호를 >= 대신 > 로 바꾸면 'A-B-C' 는 어떻게 변환될까?
#     그 결과는 A-(B-C) 인가, (A-B)-C 인가?
#
# Q3. TODO 4 (남은 '(' 제거)를 빼먹으면 '(2+3)*4' 의 결과에 무엇이 섞여 나올까?
#
# Q4. 피연산자 판별을 isalnum() 대신 isdigit() 으로 쓰면 'A+B' 는 어떻게 될까?
#
# Q5. TODO 7 (남은 연산자 pop)을 빼먹으면 '2+3' 은 무엇으로 변환될까?
