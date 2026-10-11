#################################
## 조합 ###
#################################
arr = list(range(1, 11))
N = len(arr)

# 조합
def combination(arr, r):
    if r ==0 :
        return [[]]
    
    result = []
    for i in range(len(arr)):
        elem = arr[i]
        next_arr = arr[i+1:]
        for next in combination(next_arr,r-1):
            result.append(next+[elem])

    return result

valid_subsets = []
for i in range(1, N+1):
    subset = list(combination(arr, i))
    for j in range(len(subset)):
       if sum(subset[j]) == 10:
            subset[j].sort() # sort는 원본 정렬
            valid_subsets.append(subset[j])

valid_subsets.reverse()
print('조합')
for subset in valid_subsets:
    print(*subset)



#################################
## 재귀 ###
#################################
arr = list(range(1, 11))
N = len(arr)
def find_subset(k, current_subset):
    if sum(current_subset) > 10:
        return
    if k == N:
        if sum(current_subset) == 10:
            print(*current_subset)
        return

    find_subset(k+1, current_subset + [arr[k]])
    find_subset(k+1, current_subset)

print('재귀')
find_subset(0, [])

############################
## 백트래킹 ##
############################
arr = list(range(1, 11))
N = len(arr)
included = [False] * (N)
def find_subset_backtracking(k, current_subset, included):
    if sum(current_subset) > 10 :
        return
    if k == N:
        if sum(current_subset) == 10:
            for i in range(0, N):
                if included[i]:
                    print(arr[i], end = ' ')
            print()
        return

    included[k] = True
    find_subset_backtracking(k+1, current_subset + [arr[k]],included)

    included[k] = False
    find_subset_backtracking(k+1, current_subset,included)

print('백트래킹')
find_subset_backtracking(0, [], included)




# 1 2 3 4 
# 1 2 7 
# 1 3 6 
# 1 4 5 
# 1 9 
# 2 3 5 
# 2 8 
# 3 7 
# 4 6 
# 10