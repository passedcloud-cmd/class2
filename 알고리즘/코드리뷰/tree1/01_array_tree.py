# 1단계: 1차원 배열로 트리 표현하기 (완전 이진 트리)
#
# 코드는 완성되어 있습니다
# 
# 학습 목표
#   - 연결 정보 없이 '인덱스 규칙' 만으로 트리를 표현할 수 있다.
#   - 부모 i 에 대해 왼쪽 자식은 i * 2, 오른쪽 자식은 i * 2 + 1 임을 이해한다.
#   - 0번 인덱스를 왜 비워 두는지 설명할 수 있다.
#
# 시간 복잡도: 부모/자식 조회 O(1)
# 공간 복잡도: O(N)  - 노드 수 N + 더미 1칸

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '01_input.txt')

N = int(input())
raw_data = input().split()  # ['A', 'B', 'C', 'D', 'E', 'F']

# [실습 1] 트리 저장소 만들기
#   i * 2 규칙이 성립하려면 루트가 반드시 1번 인덱스에 있어야 합니다.
#   raw_data 를 그대로 쓰면 루트가 0번에 들어가 규칙이 깨집니다.
#   앞에 무엇을 하나 붙이면 될까요?
tree = [0] + raw_data  # TODO: 0번 인덱스를 더미로 채워 루트를 1번으로 밀어내세요

print('=== 1차원 배열 트리 생성 완료 ===')
print(f'인덱스 : {list(range(len(tree)))}')
print(f'데이터 : {tree}')
print()


def get_family(idx):
    """idx번 노드의 부모 / 왼쪽 자식 / 오른쪽 자식을 출력한다."""
    if idx >= len(tree):
        print(f'[인덱스 {idx}] 범위를 벗어난 노드입니다.')
        return

    print(f'[노드 {tree[idx]} (인덱스 {idx})]')

    # [실습 2] 부모 인덱스 구하기
    #   자식에서 부모로 올라가는 계산입니다. 나눗셈을 씁니다.
    #   루트(1번)는 계산 결과가 0이 되어 '부모 없음' 으로 걸러집니다.
    #   (루트는 1 // 2 == 0 이므로 부모가 없다.)
    parent_idx = idx // 2  # TODO

    if parent_idx >= 1:
        print(f'  - 부모       : {tree[parent_idx]} (인덱스 {parent_idx})')
    else:
        print('  - 부모       : 없음 (루트)')

    # [실습 3] 왼쪽 자식 인덱스 구하기
    left_idx = idx * 2  # TODO

    if left_idx < len(tree):
        print(f'  - 왼쪽 자식  : {tree[left_idx]} (인덱스 {left_idx})')
    else:
        print('  - 왼쪽 자식  : 없음')

    # [실습 4] 오른쪽 자식 인덱스 구하기
    #   왼쪽 자식 바로 옆 칸입니다.
    right_idx = idx * 2 + 1  # TODO

    if right_idx < len(tree):
        print(f'  - 오른쪽 자식: {tree[right_idx]} (인덱스 {right_idx})')
    else:
        print('  - 오른쪽 자식: 없음')

    print()


for i in range(1, N + 1):
    get_family(i)

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 레벨 n 은 인덱스 2**n 에서 시작해 2**(n+1) - 1 에서 끝난다.
print('=== 레벨별 인덱스 배정 ===')
last = len(tree) - 1
level = 0
while 2**level <= N:
    start = 2**level
    end = 2 ** (level + 1) - 1
    nodes = ' '.join(f'{tree[i]}({i})' for i in range(start, min(end, last) + 1))
    print(f'레벨 {level} | 인덱스 {start} ~ {end} | {nodes}')
    level += 1

print()
print(f'높이 h = {level - 1} 인 트리의 최대 노드 수 : {2 ** level - 1}')
print(f'필요한 리스트 크기 (더미 1칸 포함)   : {2 ** level}')
