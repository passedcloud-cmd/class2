# 3단계: 트리 순회 3종 (전위 / 중위 / 후위)
# 
# 세 순회는 모두 재귀이며, '나(V)를 언제 처리하는가' 만 다르다.
#
# 학습 목표
#   - 세 순회의 차이가 'print 한 줄의 위치' 뿐임을 설명할 수 있다.
#   - 재귀의 기저 조건이 왜 node == 0 인지 설명할 수 있다.
#   - 주어진 트리에 대해 세 순회 결과를 손으로 먼저 적어보고 코드로 검증할 수 있다.

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '03_input.txt')

# 편향 트리처럼 깊이가 깊어지면 파이썬 기본 재귀 한계(1000)에 걸려
# RecursionError 가 난다. 트리/그래프 문제에서는 거의 관용구처럼 올려 둔다.
sys.setrecursionlimit(10**6)


# 전위 순회는 예시로 완성해 두었습니다. 아래 두 함수를 같은 방식으로 채워보세요.
def preorder(node):
    """V -> L -> R : 나를 가장 먼저 처리한다."""
    if node == 0:
        return

    print(node, end=' ')  # V: 나
    preorder(left[node])  # L: 왼쪽
    preorder(right[node])  # R: 오른쪽


# [실습 1] 중위 순회 (L -> V -> R)
#   왼쪽을 끝까지 다 본 뒤에 나를 출력하고, 그 다음 오른쪽으로 갑니다.
#   preorder 와 비교해 '무엇이 몇 칸 움직였는지' 만 보면 됩니다.
def inorder(node):
    """L -> V -> R : 왼쪽을 다 본 뒤 나를 처리한다."""
    if node == 0:
        return

    inorder(left[node])  # L: 왼쪽
    print(node, end=' ')  # V: 나
    inorder(right[node])  # R: 오른쪽


# [실습 2] 후위 순회 (L -> R -> V)
#   양쪽을 다 본 뒤 마지막에 나를 출력합니다.
def postorder(node):
    """L -> R -> V : 양쪽을 다 본 뒤 마지막에 나를 처리한다."""
    if node == 0:
        return

    postorder(left[node])  # L: 왼쪽
    postorder(right[node])  # R: 오른쪽
    print(node, end=' ')  # V: 나


# --- 트리 만들기 (02번 파일에서 작성한 코드 사용) ---
V = int(input())
E = V - 1
edge = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    parent = edge[i * 2]
    child = edge[i * 2 + 1]

    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

# --- 순회 실행 ---
root = 1

print('전위 순회(VLR): ', end='')
preorder(root)
print()

print('중위 순회(LVR): ', end='')
inorder(root)
print()

print('후위 순회(LRV): ', end='')
postorder(root)
print()
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 들여쓰기 한 칸 = 재귀 한 단계. 호출과 종료가 상자처럼 짝을 이룬다.
# 전체를 다 찍으면 너무 길어지므로 왼쪽 서브트리(2번)만 따라가 본다.
print('=== 전위 순회 재귀 호출 과정 (일부) ===')
visited = []


def preorder_trace(node, depth=0, label='시작'):
    pad = '  ' * depth

    if node == 0:
        print(f'{pad}{label}: preorder(0) -> 아무것도 안 하고 반환')
        return

    print(f'{pad}{label}: preorder({node}) 호출')
    visited.append(node)
    print(f'{pad}    V: {node} 출력  (현재 출력: {" ".join(map(str, visited))})')

    preorder_trace(left[node], depth + 1, 'L')
    preorder_trace(right[node], depth + 1, 'R')

    print(f'{pad}   preorder({node}) 종료')


preorder_trace(2)

print()
print('=== 세 순회 비교 ===')
print('전위 VLR | 나 -> 왼 -> 오 | 트리 복사/저장, 디렉터리 출력')
print('중위 LVR | 왼 -> 나 -> 오 | BST 정렬 출력, 수식의 중위 표기')
print('후위 LRV | 왼 -> 오 -> 나 | 수식 트리 계산(04번), 트리 삭제')
print()
print('고르는 기준: "부모 일을 하려면 자식 결과가 필요한가?"')
print('  필요하다  -> 후위 (자식을 먼저 끝내야 하므로)')
print('  필요없다  -> 전위 (위에서부터 뿌리면 되므로)')

# [예고] 레벨 순회 (너비 우선, BFS)
# 위 세 가지는 모두 '재귀 = 스택' 을 써서 한 갈래를 끝까지 파고 들어간다.
# 반대로 큐(collections.deque)를 쓰면 한 층씩 훑는 '레벨 순회' 가 된다.
# 이 트리에서는 결과가 1 2 3 4 ... 13 으로 노드 번호 순서와 똑같이 나온다.
# 스택으로 가면 깊이 우선, 큐로 가면 너비 우선 - 그래프 단원(DFS/BFS)에서 본격적으로 다룬다.
