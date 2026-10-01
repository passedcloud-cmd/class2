# # 주사위 n개 던졌을 때 나올 수 있는 경우
# n = int(input())
# path = [0] * n

# def abc(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(1, 7):
#         path[level]=i
#         abc(level+1)

# abc(0)





# # 로컬 변수와 글로벌 변수의 차이. 로컬 변수는 함수 내에서 입력받은 매개변수로 작동
# # 재귀 이용해서 출력해보기
# def abc(level):
#     print(level, end = ' ')
#     if level == 3:
#         return

#     abc(level + 1)
#     print(level, end = ' ')

# abc(0) # 0 1 2 3 2 1 0

# print()
# def abc2(level):
#     if level == 6:
#         return
    
#     print(level, end = ' ')
#     abc2(level + 1)
#     print(level, end = ' ')

# abc2(0) #0 1 2 3 4 5 5 4 3 2 1 0 






# 누적합 구하기 - 재귀 DFS 구현 시 변수를 global 선언하는지 매개변수에 선언하는지에 따른 차이
arr = [1,3,5,7]
Sum = arr[0]

def abc(level):
    global Sum

    if level == 3:
        print(Sum, end= ' ')
        return

    Sum += arr[level+1]
    abc(level+1)
    print(Sum, end = ' ') # Sum이 전역변수이기 때문에 계속 16인 채로 남음!

# abc(0) #16 16 16 16

def abc2(level):
    global Sum

    if level == 3:
        print(Sum, end= ' ')
        return

    Sum += arr[level+1]
    abc2(level+1)
    Sum -= arr[level+1] # Sum 전역변수니까 값 빼주기
    print(Sum, end = ' ') 

# abc2(0) # 16 9 4 1 


def abc3(level,Sum):
    if level ==3:
        print(Sum,end=' ')
        return

    abc3(level+1, Sum+arr[level+1])
    print(Sum, end=' ')

# abc3(0, arr[0])



# 레벨 4짜리 2진 트리
def abc4(level):
    ####################################코드가 들어갈 수 있는 자리
    if level == 4: # level
        ####################################
        return
    
    ####################################
    for i in range(2): # 가지 수가 2
        ####################################    
        abc4(level+1)
        ####################################

    ####################################
# abc4(0)


# ABCD 카드묶음에서 카드를 3번 뽑기 - 중복 뽑기 가능
# level =3  
# branch = 4
card = "ABCD"
path = [""]*3 # 경로를 저장하는 배열. 크기는 level

def abc5(level):
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
        
    for i in range(4):
        path[level]=card[i]
        abc5(level+1)
        # path[level] = 0 # 경로 지우기. 경로 안 지우면 기존에 있는 level의 값을 다음 카드가 덮어버림. 
        # 지금은 없어도 됨

# abc5(0)




# # 주사위 던지기
# n = int(input()) # 주사위 개수 n
# path = [0]*n
# def abc6(level):
#     if level == n:
#         print(*path)
#         return

#     for i in range(1,7):
#         path[level]=i # 앞으로 들어갈 곳을 path 배열에 기록
#         abc6(level+1)

# abc6(0)





# # 중복이 안되는 순열
# card = "ABCD"
# path = [""] * 3 # level (depth 크기)
# used = [0] * 4 # branch 크기
# def abc7(level):
#     if level == 3:
#         print(*path)
#         return
        
#     for i in range(4):
#         if used[i]==1: continue
#         used[i] = 1
#         path[level]=card[i]
#         abc7(level+1)
#         path[level] = 0 # 경로 지우기.
#         used[i]=0 # 방문체크 해제


# abc7(0)




## 수정할 것
# 합이 10 이상인 경우는 몇 가지
arr8 = [3,4,7,1,6]
cnt = 0
Sum = 0
def abc8(level):
    global cnt, Sum

    # if Sum>10: # 가지치기
    #     return
    
    if level ==3:
        if Sum >= 10:
            cnt +=1
        return

    for i in range(5):
        Sum+=arr8[i]
        abc8(level+1)
        Sum-=arr8[i]

abc8(8)
print(cnt)