
# ################################
# #부분집합########################
# ###############################
# name = "ABC"
# def abc(level,path):
#     if level == 3:
#         print(*path)
#         return

#     abc(level+1,path)
#     abc(level+1, path+[name[level]])

# abc(0,[])




arr=['A', 'B', 'C']
n=len(arr)

for tar in range(1<<n): # 1 x 2^n
    answer =[]
    for i in range(n): # 모든 스위치를 하나씩 검사
        if tar&1: # 결과가 1이면 지금 보는 스위치가 켜져 있다
            answer.append(arr[i])
        tar>>=1 # target 값을 오른쪽으로 한 칸 민다. 110 -> 011 -> 001 -> 000
    print(answer)




# arr=['A', 'B', 'C', 'D', 'E']
# n=len(arr)

# for tar in range(1<<n): # 1 x 2^n
#     answer =[]
#     for i in range(n):
#         if tar&1:
#             answer.append(arr[i])
#         tar>>=1 # target 값을 오른쪽으로 한 칸 민다. 110 -> 010 -> 001 -> 000
#     if len(answer) >=2: # 최소 2명 이상이 카페에 간다면
#         print(answer)





## 중복 순열
# card = "ABCD"
# path=[""]*3 # 카드 묶음의 개수

# def abc(level): #중복 순열 # level = "지금 몇 번째 칸을 채울 차례인가" (0, 1, 2)
#     if level ==3:  # 0, 1, 2번 칸을 다 채웠다면
#         print(*path) # 완성된 조합을 출력하고
#         return # 이전 단계로 돌아가기

#     for i in range(4):
#         path[level]=card[i] #지금 칸에 카드를 넣고
#         abc(level+1) # 다음 칸을 채우러 가기 (자기 자신을 다시 부름)
#         path[level]="" # 돌아오면 칸을 비우기 (정리) # 백트래킹 방법. 지금은 없어도 되긴 함

# abc(0)




# ## 순열
# card = "ABCD"
# path=[""]*3 # 카드 묶음의 개수
# used=[0]*4 # 선택할 수 있는 카드 종류의 개수(branch)

# def abc(level): #순열
#     if level ==3:
#         print(*path)
#         return

#     for i in range(4):
#         if used[i]==1: continue
#         used[i]=1
#         path[level]=card[i]
#         abc(level+1)
#         path[level]=""
#         used[i]=0

# abc(0)




# ## 조합
# card = "ABCD"
# path = [""]*3 # 카드 묶음의 개수
# def abc(level, start):
#     if level == 3:
#         print(*path)
#         return

#     for i in range(start, 4):
#         path[level]=card[i] # 내가 앞으로 들어갈 경로를 적고
#         abc(level+1, i+1) #다음 함수에 진입. 다음 level에선 i+1번째 카드만 넣음. 중복을 피하기 위해
#         path[level]= ""   # 함수 리턴 후 적었던 경로를 지우기. 현재에선 없어도 됨. 다음 경로로 덮어질 거니.

# abc(0,0)



# ## 중복 조합
# card = "ABCD"
# path = [""]*3 # 카드 묶음의 개수
# def abc(level, start):
#     if level == 3:
#         print(*path)
#         return

#     for i in range(start, 4):
#         path[level]=card[i] 
#         abc(level+1, i) # 다음 level에 i번째 카드 넣으면 중복 조합. 조합은 i+1번째부터, 중복 조합은 i번째부터
#         path[level]= ""  

# abc(0,0)





# # 동전 교환 - 탐욕
# coin = [500, 50, 100, 10]
# target= 1110
# coin.sort(reverse=True) # [500, 100, 50, 10]

# cnt = 0 # 사용한 동전 개수
# for i in range(4):
#     temp=target//coin[i] # coin[i]의 개수
#     cnt+=temp
#     target=target-(temp*coin[i])
# print(cnt)



# # 화장실 문제
# poo = [15, 30, 50, 10]
# poo.sort() # [10, 15, 30, 50]
# sum = 0
# for i in range(3,0,-1):  # 대기 인원
#     sum += (i*poo[3-i])
# print(sum) # 누적 대기 시간



# # knapsack 문제 - 탐욕 x. 완전탐색 o
# # fractional knapsack - 탐욕 o
# bag = 30 # 30kg 담을 수 있음
# salt = [(5,50), (10,60), (20,140)] # 죽염 5kg당 50만원, 히말라야 10kg당 60만, 천일염 20kg당 140만
# # 키로당 단가가 높은 순서로 sort
# salt.sort(key=lambda x:x[1]//x[0], reverse=True)
# print(salt)

# total_value = 0 # 가방의 총 가치
# for weight, price in salt:
#     # 다 담을 수 있다면
#     if bag >= weight:
#         bag-=weight # 담은만큼 가방 무게 빼고
#         total_value+=price # 가방의 가치를 업데이트
#     # 다 담을 수 없다면, 가방에 담을 수 있는 가치 = 남은 가방 무게 * 담는 물건의 단가
#     else:
#         total_value+=(bag*(price//weight))
#         bag = 0
#         break
# print(total_value)



# # 람다식
# result=(lambda a,b:a+b)(3,4)
# print(result)

# result2=(lambda a,b:a+b)
# print(result2(5,6))



# # sort
# def test(x):
#     return -x

# arr=[12,3,3,4,5,6,1]
# arr.sort(key=test)
# print(arr)

# arr.sort(key=lambda x:-x)
# print(arr)
