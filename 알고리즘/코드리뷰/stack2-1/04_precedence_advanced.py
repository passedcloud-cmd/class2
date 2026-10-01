# ------------------------------------------------------------
# 04. [심화] isp / icp 와 예외 처리
# ------------------------------------------------------------
# [참고 수준] 이 파일은 참고용입니다.
#   기본 문제 풀이에는 01~03번으로 충분하며, 거듭제곱(^)이 나오는 유형은 흔하지 않습니다.
#   "이런 것도 있구나" 정도로 확인하고, 여유가 있을 때 채워보세요.
#
# 02번에서는 우선순위를 값 하나(precedence)로만 다뤘다.
# 그런데 실제 이론에서는 우선순위를 '두 개' 로 나눠서 본다.
#
#   isp (In-Stack Precedence)    : 스택 '안'에 있는 연산자의 우선순위
#   icp (In-Coming Precedence)   : 새로 들어오는(아직 push 안 된) 연산자의 우선순위
#
#   토큰      isp   icp   특징
#   -------- ----- ----- ------------------------------------------------
#   (          0     4   스택 안에서는 가장 낮게, 새로 들어올 때는 가장 높게
#   ^          3     4   거듭제곱은 오른쪽 결합성 때문에 icp 를 1 크게
#   *, /       2     2
#   +, -       1     1
#
# [규칙] while stack and isp[stack[-1]] >= icp[token]:  pop
#
# [왜 두 개로 나누나]
#   1. '(' 는 새로 들어올 때 아무도 밀어내지 않아야 하고(icp 최고),
#      스택에 들어간 뒤에는 아무도 밀어내지 못해야 한다(isp 최저).
#      값 하나로는 이 두 성질을 동시에 표현할 수 없다.
#   2. '^' 는 오른쪽 결합성이라, 같은 '^' 가 들어와도 pop 하지 않아야 한다.
#      icp 를 isp 보다 1 크게 두면 isp >= icp 가 거짓이 되어 자동으로 push 된다.
# ------------------------------------------------------------

# [오른쪽 결합성이란]
#   연산자가 연달아 나올 때 오른쪽 연산부터 먼저 계산하는 규칙.
#     왼쪽 결합성 : 10 - 5 - 2  =>  (10 - 5) - 2 = 3     (+, -, *, / 가 여기 해당)
#     오른쪽 결합성: 2 ^ 3 ^ 2  =>  2 ^ (3 ^ 2) = 2^9 = 512
#                    만약 왼쪽 결합이면 (2^3)^2 = 64 로 답이 달라진다.

ISP = {'(': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
ICP = {'(': 4, '^': 4, '*': 2, '/': 2, '+': 1, '-': 1}


def infix_to_postfix_advanced(expression):
    """isp / icp 를 구분해 ^ 까지 처리하는 변환기"""
    stack = []
    result = []

    for token in expression:
        # 1. 피연산자는 바로 결과로
        if token.isalnum():
            result.append(token)

        # 2. 닫는 괄호는 특별 취급: '(' 를 만날 때까지 pop
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '(' 제거 (출력 X)

        # 3. 그 외 연산자와 '(' 는 같은 규칙으로 처리
        #    '(' 는 icp 가 4로 가장 높아서 아무것도 pop 하지 않고 그냥 push 된다
        else:
            while stack and ISP[stack[-1]] >= ICP[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


print('=== isp / icp 방식 변환 ===')
cases = [
    ('(2+3)*4', '23+4*'),
    ('2+3*4-5', '234*+5-'),
    ('2^3^2', '232^^'),  # 오른쪽 결합성: 2^(3^2)
    ('2*3^2', '232^*'),  # ^ 가 * 보다 우선
    ('A-B-C', 'AB-C-'),  # 왼쪽 결합성: (A-B)-C
]
for infix, expected in cases:
    actual = infix_to_postfix_advanced(infix)
    mark = 'O' if actual == expected else 'X'
    print(f'  {infix:<10} -> {actual:<10} (기대: {expected:<10}) {mark}')


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] ^ 가 왜 pop 되지 않는지 확인하기
# ------------------------------------------------------------
def trace_advanced(expression):
    """isp / icp 비교 결과를 함께 출력"""
    stack = []
    result = []
    print(f'  중위 표기식: {expression}')
    print(f'  {"토큰":<4} {"비교":<28} {"판정":<10} {"스택":<14} {"결과"}')
    print(f'  {"-" * 4} {"-" * 28} {"-" * 10} {"-" * 14} {"-" * 8}')

    for token in expression:
        if token.isalnum():
            result.append(token)
            print(f'  {token:<4} {"피연산자":<28} {"결과로":<10} {stack!s:<14} {"".join(result)}')
            continue

        if token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
            print(f'  {token:<4} {"( 만날 때까지 pop":<28} {"":<10} {stack!s:<14} {"".join(result)}')
            continue

        while stack and ISP[stack[-1]] >= ICP[token]:
            top = stack[-1]
            compare = f'isp[{top}]={ISP[top]} >= icp[{token}]={ICP[token]}'
            result.append(stack.pop())
            print(f'  {token:<4} {compare:<28} {"참 -> pop":<10} {stack!s:<14} {"".join(result)}')

        if stack:
            top = stack[-1]
            compare = f'isp[{top}]={ISP[top]} >= icp[{token}]={ICP[token]}'
        else:
            compare = '스택 비어있음'
        stack.append(token)
        print(f'  {token:<4} {compare:<28} {"거짓 -> push":<10} {stack!s:<14} {"".join(result)}')

    while stack:
        result.append(stack.pop())
    print(f'  {"끝":<4} {"남은 연산자 전부 pop":<28} {"":<10} {"[]":<14} {"".join(result)}')


print('=== 2^3^2 - 오른쪽 결합성 ===')
trace_advanced('2^3^2')
print('  isp[^]=3 >= icp[^]=4 가 거짓이므로 pop 하지 않고 쌓인다 => 232^^')

print()
print('=== A-B-C - 왼쪽 결합성 (비교) ===')
trace_advanced('A-B-C')
print('  isp[-]=1 >= icp[-]=1 은 참이므로 pop 된다 => AB-C-')


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [주의] 파이썬에서 ^ 는 거듭제곱이 아니다
# ------------------------------------------------------------
#   구분           기호   의미              비고
#   ------------- ------ ---------------- -------------------------------
#   알고리즘 이론    ^     거듭제곱          우선순위 최고, 오른쪽 결합
#   Python 코드    ^     비트 연산 (XOR)   2 ^ 3 은 1 이 나온다 (완전 다름)
#   Python 코드    **    거듭제곱          실제 계산에는 이걸 써야 한다
print('=== ^ 와 ** 의 차이 ===')
print(f'  파이썬에서  2 ^ 3  = {2 ^ 3}   <- XOR 비트 연산')
print(f'  파이썬에서  2 ** 3 = {2 ** 3}   <- 거듭제곱')
print('  => 변환 과정에서는 기호로 ^ 를 쓰되, 계산할 때는 ** 로 처리해야 한다.')


def evaluate_postfix_advanced(expression):
    """^ 를 거듭제곱으로 계산하는 후위 계산기"""
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
            elif token == '^':
                stack.append(left**right)  # ^ 가 아니라 ** 로 계산
    return stack.pop()


print()
print('=== 거듭제곱까지 계산해 보기 ===')
for infix in ['2^3^2', '2*3^2', '2^3+1']:
    postfix = infix_to_postfix_advanced(infix)
    print(f'  {infix:<8} -> {postfix:<8} = {evaluate_postfix_advanced(postfix)}')
print('  2^3^2 는 2^(3^2) = 2^9 = 512 여야 한다. 64 가 나오면 결합성 처리가 틀린 것이다.')


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [예외 처리] 올바르지 않은 수식 다루기
# ------------------------------------------------------------
# 1. 피연산자 부족 (Stack Underflow) : '5 +'   연산자를 만났는데 숫자가 부족
# 2. 0으로 나누기                    : '5 0 /' 런타임 에러
# 3. 수식 종료 후 잔여 데이터         : '5 3'   연산자 누락, 스택에 2개 이상 남음
def safe_evaluate(expression):
    """세 가지 예외를 모두 검사하는 안전한 계산기 (공백 구분)"""
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue

        # 예외 1) 피연산자 부족
        if len(stack) < 2:
            return f'Error: 피연산자가 부족합니다 (토큰 {token!r})'

        right = stack.pop()
        left = stack.pop()

        # 예외 2) 0으로 나누기
        if token == '/' and right == 0:
            return 'Error: 0으로 나눌 수 없습니다'

        if token == '+':
            stack.append(left + right)
        elif token == '-':
            stack.append(left - right)
        elif token == '*':
            stack.append(left * right)
        elif token == '/':
            stack.append(int(left / right))
        elif token == '^':
            stack.append(left**right)
        else:
            return f'Error: 알 수 없는 연산자 {token!r}'

    # 예외 3) 잔여 데이터 - 정상이면 딱 1개만 남아야 한다
    if len(stack) != 1:
        return f'Error: 수식이 올바르지 않습니다 (스택에 {len(stack)}개 남음)'

    return stack[0]


print('=== 예외 처리 확인 ===')
print(f'  {"입력":<16} | 결과')
print(f'  {"-" * 16} | {"-" * 40}')
for expr in ['10 20 + 3 *', '5 +', '5 0 /', '5 3', '2 3 ^', '5 3 %']:
    print(f'  {expr:<16} | {safe_evaluate(expr)}')

# [포인트] 예외를 잡지 않으면 IndexError, ZeroDivisionError 로 프로그램이 죽는다.
#          "죽지 않고, 무엇이 잘못됐는지 알려주는 것" 이 예외 처리의 목적이다.
