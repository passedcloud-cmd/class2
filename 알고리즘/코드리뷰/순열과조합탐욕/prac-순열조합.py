for i in range(1,4):
    for j in range(1,4):
        if i != j:
            for k in range(1,4):
                if j !=k and i !=k:
                    print(f'for문 순열: {i,j,k}')

for i in range(1,4):
    for j in range(1,4):
            for k in range(1,4):
                    print(f'for문 중복순열: {i,j,k}')

def permutation(selected, remaining, r):
    if len(selected) == r:
        print(f'순열: {selected}')
        return

    for i in range(len(remaining)):
        pick = remaining[i]
        next_remainig = remaining[:i] +remaining[i+1:]
        permutation(selected + [pick], next_remainig, r)

permutation([], [1, 2, 3], 2)


## 리스트로 내뱉은 순열
def permutation(arr, r):
    result = []

    def pick_next(selected, remaining):
        if len(selected) == r:
            result.append(selected)
            return
        for i in range(len(remaining)):
            pick = remaining[i]
            next_remaining = remaining[:i]+remaining[i+1:]
            pick_next(selected+[pick], next_remaining)
    pick_next([], arr)
    return result

ans = permutation([1,2,3,4], 2)
print(ans)





def rep_permutation(selected, remaining, r):
    if len(selected) == r:
        print(f'중복 순열: {selected}')
        return

    for i in range(len(remaining)):
        pick = remaining[i]
        rep_permutation(selected + [pick], remaining, r)

rep_permutation([], [1, 2, 3], 2)

import itertools
data_list = ['A', 'B', 'C', 'D']
result = list(itertools.permutations(data_list, 2))
print(f'itertools 순열:',list(map(''.join,result)))

print(f'itertools 순열:', end = ' ')
for perm_tuple in itertools.permutations(data_list,2):
    print(''.join(perm_tuple), end = ' ')

result = list(itertools.product(data_list, repeat = 2))
print()
print(f'itertools 중복순열:',list(map(''.join,result)))

##########################################################

numbers = [1,2,3,4]
n = len(numbers)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            print(numbers[i], numbers[j], numbers[k])

def combination(arr, r):
    if r == 0:
        return [[]]

    result = []
    for i in range(len(arr)):
        elem = arr[i]
        next_arr = arr[i+1:]
        for rest in combination(next_arr, r-1):
            result.append([elem]+rest)

    return result

data = [1, 2, 3, 4]
print('조합')
print(list(combination(data, 3)))

def rep_combination(arr, r):
    if r == 0:
        return [[]]

    result = []
    for i in range(len(arr)):
        elem = arr[i]
        for rest in rep_combination(arr, r-1):
            result.append([elem]+rest)

    return result

data = [1, 2, 3, 4]
# rep_combination(data, 2)
print('중복 조합')
print(list(rep_combination(data, 2)))

import itertools
data = [1, 2, 3, 4]
result = list(itertools.combinations(data,2))
print(f'itertools 순열:', result)

result = list(itertools.combinations_with_replacement(data,2))
print(f'itertools 중복순열:', result)