# ------------------------------------------------------------
# 03. 두 기능을 합쳐 계산기 완성하기
# ------------------------------------------------------------
# [두 가지 스택의 역할 비교]  <- 이 단원에서 가장 헷갈리는 지점
#
#   구분        | 02. 중위 -> 후위 변환            | 01. 후위 표기법 계산
#   ----------- | -------------------------------- | ---------------------------
#   목표        | 사람의 식을 컴퓨터 식으로 번역   | 번역된 식을 실제로 계산
#   스택의 용도 | 연산자(+, - 등) 보관소           | 피연산자(숫자) 보관소
#   처리 규칙   | 우선순위 높은 연산자가 먼저 나옴 | 연산자를 만나면 숫자를 꺼내 계산
#   결과물      | 문자열 (예: '23+')               | 숫자 (예: 5)
#
# [학습 목표] 같은 '스택'이지만 무엇을 담느냐가 정반대다.
#             이 둘을 이어 붙여 진짜 계산기를 완성한다.
# ------------------------------------------------------------


# ============================================================
# 1. 여러 자리 숫자 처리하기 (공백으로 토큰 구분)
# ============================================================
# 01번 코드는 '53+2*' 처럼 피연산자가 '한 자리' 일 때만 동작했다.
# '12' 는 문자 '1', '2' 로 쪼개져 읽히기 때문이다.
# => 실제로는 토큰을 공백으로 구분하고 split() 으로 나눈다.
def calculate_expression(expression):
    # TODO 1) 공백을 기준으로 문자열을 잘라 리스트로 만드세요.
    #   힌트: '10 20 +'  ->  ['10', '20', '+']
    tokens = []
    stack = []

    for token in tokens:
        # 1. 피연산자 처리 (여러 자리 수 포함)
        # isdigit() 은 음수를 처리하지 못하므로 여기서는 양의 정수 기준
        if token.isdigit():
            # TODO 2) 01번과 같다. 정수로 바꿔 스택에 넣으세요.
            pass

        # 2. 연산자 처리
        else:
            if len(stack) < 2:
                return 'Error: 숫자가 부족합니다.'

            # TODO 3) 01번의 계산 로직을 그대로 가져오세요.
            #         right 를 먼저 꺼내고 left 를 나중에 꺼낸다는 점에 주의.
            pass

    # 정상적인 식이라면 스택에 값이 딱 하나 남아 있다
    return stack[0] if stack else 'Error: 빈 수식입니다.'


print('=== 1. 여러 자리 숫자 계산 (공백 구분) ===')
print(f"  '10 20 + 3 *'  -> {calculate_expression('10 20 + 3 *')}")  # (10+20)*3 = 90
print(f"  '100 20 /'     -> {calculate_expression('100 20 /')}")  # 100/20 = 5
print(f"  '123 456 +'    -> {calculate_expression('123 456 +')}")  # 579

# [비교] 한 자리 전용 코드로 같은 식을 처리하면?
print("\n  한 자리 전용 코드에 '12 3 +' 을 넣으면 '1','2',' ','3' 로 쪼개져 실패한다.")
print('  => 공백 구분 + split() 이 해결책이다.')


print('\n' + '=' * 60 + '\n')


# ============================================================
# 2. 변환 + 계산 = 계산기
# ============================================================
def infix_to_postfix(expression):
    """02번 파일의 변환 함수 (여기서는 완성본을 그대로 사용합니다)"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []

    for token in expression:
        if token.isalnum():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


def evaluate_postfix(expression):
    """01번 파일의 계산 함수 (여기서는 완성본을 그대로 사용합니다)"""
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


def calculator(infix_expression):
    """중위 표기식을 받아 계산 결과까지 한 번에 반환"""
    # TODO 4) 위 두 함수를 이어 붙이세요.
    #   1) 중위식을 후위식으로 번역하고
    #   2) 그 후위식을 계산해서 반환한다
    postfix = infix_to_postfix(infix_expression)
    return evaluate_postfix((postfix))


print('=== 2. 중위식 하나 넣으면 답이 나오는 계산기 ===')
print(f'  {"입력 (중위)":<14} | {"번역 (후위)":<10} | {"결과":>6}')
print(f'  {"-" * 14} | {"-" * 10} | {"-" * 6}')
for infix in ['(2+3)*4', '2+3*4-5', '8/2+1', '2*(3+4)/5', '9-2-3']:
    postfix = infix_to_postfix(infix)
    print(f'  {infix:<14} | {postfix:<10} | {calculator(infix)!s:>6}')

# [포인트] 사용자는 중위식만 던지면 된다.
#          내부에서 '번역(스택=연산자) -> 계산(스택=피연산자)' 두 단계가 돌아간다.
#          실제 계산기, 컴파일러, 인터프리터가 쓰는 원리가 바로 이것이다.


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] 두 단계를 나란히 보기
# ------------------------------------------------------------
def trace_calculator(infix_expression):
    """번역 단계와 계산 단계를 구분해서 출력"""
    print(f'  입력(중위): {infix_expression}')
    print()

    print('  [1단계] 번역  - 스택에 담기는 것: 연산자')
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []
    for token in infix_expression:
        if token.isalnum():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)
        print(f'    {token}  스택(연산자): {stack!s:<14} 결과: {"".join(result)}')
    while stack:
        result.append(stack.pop())
    postfix = ''.join(result)
    print(f'    => 후위 표기식: {postfix}')
    print()

    print('  [2단계] 계산  - 스택에 담기는 것: 숫자')
    stack = []
    for token in postfix:
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
        print(f'    {token}  스택(숫자): {stack}')
    print(f'    => 최종 결과: {stack[-1]}')


print('=== 두 단계 나란히 보기 ===')
trace_calculator('(2+3)*4')

# [확인] 1단계 스택에는 '(' 와 '+', '*' 같은 '기호' 만 들어간다.
#        2단계 스택에는 2, 3, 5, 20 같은 '숫자' 만 들어간다.
#        같은 자료구조인데 담는 것이 정반대다.


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [스스로 점검하기]
# ------------------------------------------------------------
# Q1. split() 대신 for char in expression 으로 읽으면 공백은 어느 분기로 갈까?
#
# Q2. split() 은 했는데 int() 변환을 빼먹으면 '10 20 +' 의 결과는?
#
# Q3. 변환기와 계산기가 각각은 맞는데 합치면 틀릴 때, 무엇을 먼저 출력해 봐야 할까?
#
# Q4. 위 '두 단계 나란히 보기' 출력에서 1단계 스택과 2단계 스택에
#     각각 어떤 종류의 값이 들어갔는지 비교해 보자. 무엇이 다른가?
#
# Q5. 정상적인 식이면 계산이 끝났을 때 스택에 값이 몇 개 남아야 할까?
#     2개 이상 남았다면 무엇이 잘못된 것일까? (04번에서 다룬다)
