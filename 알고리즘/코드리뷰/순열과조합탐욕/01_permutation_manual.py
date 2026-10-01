# 1단계: 순열 직접 구현하기
#
# 학습 목표
#   - '하나를 고르고, 남은 것에서 다시 고른다' 를 재귀로 옮길 수 있다.
#   - 기저 조건을 바꾸면 전부 뽑는 순열(nPn)이 일부만 뽑는 순열(nPr)이 된다는 것을 안다.
#
# 노션 '순열과 조합' 1.3.2 와 같은 코드입니다.


# ------------------------------------------------------------
# [실습 1] 전부 줄 세우기 (nPn)
# ------------------------------------------------------------
# def permutation(selected, remaining):
#     """selected 뒤에 remaining 을 줄 세우는 모든 경우를 출력합니다."""
#     # 1-1. 기저 조건: 남은 원소가 없으면 selected 를 출력하세요.
#     if not remaining:
#         # TODO
#         print(selected)
#         return

#     for i in range(len(remaining)):
#         pick = remaining[i]

#         # 1-2. pick 을 뺀 나머지 리스트를 만드세요.
#         #      pick 의 앞부분 remaining[:i] 와 뒷부분 remaining[i + 1 :] 을 이어 붙입니다.
#         #      '나 빼고 앞뒤 모두 챙겨서 넘긴다' 입니다.
#         next_remaining = remaining[:i] + remaining[i+1:]  # TODO

#         permutation(selected + [pick], next_remaining) # selected에 현재 pick한 것을 합쳐서 넘기기


# print('=== [1, 2, 3] 전부 줄 세우기 ===')
# permutation([], [1, 2, 3])
# print('(정답: [1, 2, 3] 부터 [3, 2, 1] 까지 6줄)')
# print()


def permutation_prac(selected, remaining):
    if not remaining:
        print(selected)
        return

    for i in range(len(remaining)):
        pick = remaining[i]

        next_remaining = remaining[:i] + remaining[i+1:]
        permutation_prac(selected + [pick], next_remaining)

permutation_prac([], [1,2,3])









# ------------------------------------------------------------
# [실습 2] r개만 뽑아 줄 세우기 (nPr)
# ------------------------------------------------------------
def permutation_r(selected, remaining, r):
    """remaining 에서 r개만 골라 줄 세우는 모든 경우를 출력합니다."""
    # 2-1. 기저 조건을 바꾸세요.
    #      '남은 게 없을 때' 가 아니라 '이미 r개를 골랐을 때' 멈춰야 합니다.
    #      멈출 때 selected 를 출력하는 것은 실습 1과 같습니다.
    if len(selected) == r:  # TODO
        print(selected)
        return

    for i in range(len(remaining)):
        pick = remaining[i]
        next_remaining = remaining[:i] + remaining[i + 1 :]
        permutation_r(selected + [pick], next_remaining, r)


print('=== [1, 2, 3, 4] 중 2개 줄 세우기 ===')
permutation_r([], [1, 2, 3, 4], 2)
print('(정답: [1, 2] [1, 3] [1, 4] [2, 1] ... [4, 3] 까지 12줄)')
