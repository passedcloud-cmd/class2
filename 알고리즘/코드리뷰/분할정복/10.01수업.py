## 분할정복 핵심 코드
# arr = [2,3,5,7,1,2,5,9]
# start = 0
# end = 7
# mid = (start+end)//2

# a = start
# b = mid+1
# result = []

# while 1:
#     if a>mid and b>end: break
#     if a>mid:
#         result.append(arr[b])
#         b+=1
#     elif b>end:
#         result.append(arr[a])
#         a+=1
#     elif arr[a]<=arr[b]:
#         result.append(arr[a])
#         a+=1
#     else:
#         result.append(arr[b])
#         b+=1
# print(*result)



## 분할정복 - 함수가 전위탐색?
# arr=[2,7,5,3,1,6,9,2]

# def merge(start,end):
#     if start==end:
#         return
#     mid=(start+end)//2

#     merge(start,mid)
#     merge(mid+1, end)

#     a = start
#     b = mid+1
#     result = []

#     while 1:
#         if a>mid and b>end: break
#         if a>mid:
#             result.append(arr[b])
#             b+=1
#         elif b>end:
#             result.append(arr[a])
#             a+=1
#         elif arr[a]<=arr[b]:
#             result.append(arr[a])
#             a+=1
#         else:
#             result.append(arr[b])
#             b+=1

#     for i in range(len(result)):
#         arr[start+i]=result[i]
    
# merge(0,7)
# print(*arr)


# a는 피벗보다 큰 수가 나올때까지 뒤로 이동
# b는 피벗보다 작거나 같은 수가 나올때까지 앞으로 이동
# 둘이 엇갈리면 break
# a,b가 자리 잡으면 a값과 b값을 swap
# 맨 마지막에 b의값고 피벗값 swap


# 퀵소트 핵심 코드
# arr= [4,7,1,6,2,8,5,3,9]
# start=0
# end=8
# pivot=start
# a=start+1
# b=end
# while 1:
#     while a<=end and arr[a]<=arr[pivot]: a+=1 # 배열범위 안이고. a의 값이 pivot보다 작다면
#     while b>=start and arr[b]>arr[pivot]: b-=1 # 배열범위 안 + b의 값이 pivot보다 크다면
#     if a>b: break
#     arr[a], arr[b] = arr[b], arr[a]

# arr[b], arr[pivot] = arr[pivot], arr[b]
# print(*arr)



# # 퀵소트- 전위탐색?
# arr= [4,7,1,6,2,8,5,3,9]

# def quick(start,end):
#     if start>=end:
#         return
#     pivot=start
#     a=start+1
#     b=end
#     while 1:
#         while a<=end and arr[a]<=arr[pivot]: a+=1 # 배열범위 안이고. a의 값이 pivot보다 작다면
#         while b>=start and arr[b]>arr[pivot]: b-=1 # 배열범위 안 + b의 값이 pivot보다 크다면
#         if a>b: break
#         arr[a], arr[b] = arr[b], arr[a]

#     arr[b], arr[pivot] = arr[pivot], arr[b]


#     quick(start, b-1)
#     quick(b+1, end)

# quick(0,8)
# print(*arr)




# #이진탐색 # 정렬이 된 data를 logN 속도로 탐색
# arr = list(range(2,31,2))
# print(arr)
# arr=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# arr.sort()
# target =20
# start = 0
# end = 14 #len(arr)-1

# check = False
# while 1:
#     mid = (start+end)//2
#     if arr[mid] == target:
#         check = True
#         break
#     if arr[mid]<target:
#         start=mid+1 # 찾고자 하는 값이 중간값보다 크다면 우측탐색
#     if arr[mid]>target:
#         end=mid-1 # 찾고자 하는 값이 중간값보다 작다면 좌측 탐색
#     if start>end:
#         break

# if check:
#     print("찾았음")
# else: 
#     print("못찾음")


# arr=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# arr.sort()
# target =20
# check = False
# def binary_search(start, end):
#     global check
#     if start>end:
#         return
#     mid=(start+end)//2
#     if target == arr[mid]:
#         check = True
#         return
#     if arr[mid] < target:
#         binary_search(mid+1, end)
#     else:
#         binary_search(start, mid-1)


# binary_search(0,14)
# if check:
#     print("찾았음")
# else:
#     print("못찾았음")



#parametric search

bettery = "*******___"

def parametric_search(start,end):
    max = -1
    while 1:
        mid = (start + end) //2
        if bettery[mid] == '_':
            end = mid -1
        elif bettery[mid] == '*':
            Max=mid
            start=mid + 1
        if start>end:
            break
    return Max+1

answer = parametric_search(0,9)
print(answer)