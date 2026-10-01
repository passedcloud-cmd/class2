"""
- "왜 후위 순회인가요?" 
  "자식들이 숫자를 먼저 구해와야 부모가 더하기든 빼기든 할 수 있으니까."
"""


# 4단계: 수식 트리 계산 (SWEA 사칙연산)
#
# 학습 목표
#   - 수식 트리에서 연산자와 피연산자가 각각 어디에 놓이는지 설명할 수 있다.
#   - 왜 하필 후위 순회로 계산하는지 한 문장으로 답할 수 있다.
#   - 재귀 함수가 '값을 돌려받아 쓰는' 구조를 직접 작성할 수 있다.

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '04_input.txt')


def calc(node):
    """node 를 루트로 하는 서브트리의 계산 결과를 돌려준다."""
    # tree[node] 예시
    #   연산자일 때: ['1', '-', '2', '3']  -> 길이 4
    #   숫자일 때  : ['3', '10']           -> 길이 2

    # [실습 1] 기저 조건
    #   리프 노드(숫자)라면 더 내려갈 곳이 없습니다.
    #   자기가 가진 값을 '정수로 바꿔서' 부모에게 돌려주면 끝입니다.
    if len(tree[node]) == 2:
        return int(tree[node][1])

    # 연산자 노드라면 
    # 후위 순회 (L -> R -> V)로 왼쪽 서브트리 계산을 먼저 한다.
    L = calc(int(tree[node][2]))  # L: 왼쪽 서브트리 계산

    # [실습 2] 오른쪽 서브트리 계산하기
    #   왼쪽과 똑같은 방식입니다. 오른쪽 자식 번호는 몇 번 칸에 있을까요?
    R = calc(int(tree[node][3]))  # R: 오른쪽 서브트리 계산

    op = tree[node][1]  # V: 내 연산자로 마무리

    # 연산자별 계산 결과 돌려주기
    if op == '+':
        return L + R
    elif op == '-':
        return L - R
    elif op == '*':
        return L * R
    else:  # '/'
        return L // R  # 문제 조건에 따라 정수 나눗셈


# --- 메인 코드 ---
N = int(input())  # 노드 개수

# 입력 줄을 그대로 저장한다. (0번 인덱스는 더미)
tree = [[] for _ in range(N + 1)]

for _ in range(N):
    temp = input().split()
    # temp[0] 이 노드 번호. 이를 인덱스로 사용해 저장한다.
    tree[int(temp[0])] = temp

print('=== 입력된 트리 정보 ===')
for i in range(1, N + 1):
    kind = '숫자(리프)' if len(tree[i]) == 2 else '연산자'
    print(f'  tree[{i}] = {tree[i]}  -> {kind}')
print()

print(f'계산 결과: {calc(1)}')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 위 calc() 를 직접 채운 뒤, 값이 아래에서 위로 올라오는 순서를 대조해 보세요.
print('=== calc() 재귀 호출 과정 ===')


def calc_trace(node, depth=0):
    pad = '  ' * depth

    if len(tree[node]) == 2:
        value = int(tree[node][1])
        print(f'{pad}calc({node}) -> 리프 노드. 값 {value} 를 그대로 올려보냄')
        return value

    op = tree[node][1]
    print(f'{pad}calc({node}) -> 연산자 "{op}". 자식부터 계산해야 함')

    L = calc_trace(int(tree[node][2]), depth + 1)
    R = calc_trace(int(tree[node][3]), depth + 1)

    if op == '+':
        result = L + R
    elif op == '-':
        result = L - R
    elif op == '*':
        result = L * R
    else:
        result = L // R

    print(f'{pad}calc({node}) -> 자식이 올려준 {L}, {R} => {L} {op} {R} = {result}')
    return result


print(f'최종 결과: {calc_trace(1)}')
