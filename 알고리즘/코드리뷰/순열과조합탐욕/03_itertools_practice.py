# 3단계: itertools 로 순열과 조합 만들기
#
# 학습 목표
#   - 순열, 조합, 중복 순열, 중복 조합을 각각 어떤 함수로 만드는지 안다.
#   - itertools 결과는 한 번 쓰면 사라진다는 것을 확인한다.
#
# 노션 '순열과 조합 (with itertools)' 1 ~ 4장과 같은 내용입니다.

from itertools import combinations, combinations_with_replacement, permutations, product

data = ['A', 'B', 'C']

# 1. data 3개를 전부 줄 세우는 순열을 리스트로 만드세요.
#    permutations 의 결과는 바로 print 하면 내용이 안 보입니다. list() 로 감싸세요.
perms = []  # TODO
print(f'순열      {len(perms)}개 (정답 6)  {perms}')

# 2. data 중 2개를 뽑는 조합을 리스트로 만드세요.
combs = []  # TODO
print(f'조합      {len(combs)}개 (정답 3)  {combs}')

# 3. 같은 글자를 다시 써도 되는 2자리 나열(중복 순열)을 리스트로 만드세요.
#    product 는 개수를 두 번째 인자가 아니라 repeat= 로 넘깁니다.
prods = []  # TODO
print(f'중복 순열 {len(prods)}개 (정답 9)  {prods}')

# 4. 같은 글자를 다시 골라도 되는 2개 조합(중복 조합)을 리스트로 만드세요.
combs_wr = []  # TODO
print(f'중복 조합 {len(combs_wr)}개 (정답 6)  {combs_wr}')
print()

# --- 한 번 쓰면 사라진다 (완성되어 있습니다) ---
pair_iter = combinations(data, 2)
print('첫 번째 list():', list(pair_iter))
print('두 번째 list():', list(pair_iter))
print('=> 두 번 쓸 거라면 처음부터 list() 로 바꿔 변수에 담아 두세요.')
