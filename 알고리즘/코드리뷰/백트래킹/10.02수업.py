# DFS
# 완전탐색 - 어디까지 탐색? (중복순열)
# DFS - 탐색 순서
# 가지치기 - pruning. 굳이 탐색할 필요가 없는 영역은 탐색 안 함
# 백트래킹 - 탐색 후 돌아옴(취소)

# BFS
# 완전탐색
# BFS
# flood fill




# 4 x 4
# branch 4 // level 4
# vertical = [j]
# seven = [i+j]
# five = [i-j+n]

# N x N 사이즈의 체스판에 N개의 퀸을 방해 없이 놓을 수 있을 경우
# 그 경우가 몇 가지 인가요?? 8 입력 / 92 출력

# n  = int(input()) #체스판의 크기
# n = 4
# vertical = [0] * n
# seven = [0]*(2*n)
# five = [0]*(2*n)

# cnt = 0
# def abc(level):
#     global cnt
#     if level == n:
#         cnt+=1
#         return

#     for j in range(n):
#         # 중복 체크
#         if vertical[j] == 1: continue
#         if seven[level+j] == 1 or five[level-j+n] ==1: continue
#         vertical[j], seven[level+j], five[level-j+n] = 1,1,1
#         abc(level+1)
#         vertical[j], seven[level+j], five[level-j+n] = 0,0,0

# abc(0)
# print(cnt)





# 자료구조? 데이터를 어떻게 저장 또는 관리할 것인가?
# 데이터를 저장하는 방식에 따라
    # 선형 자료구조: 리스트, linked list(연결리스트). 데이터의 추가 삭제가 잦으면 연결리스트 사용
        # for/while 많이 사용
    # 비선형 자료구조: 그래프(트리)
        # DFS / BFS 사용



# 연결 리스트
# 파이썬에서 연결 리스틀르 쓰려면 class 불러와야 함
class Node:
    def __init__(self,value):
        self.value = value # 인스턴스에 저장될 값
        self.next = None # 참조하고 있는 객체가 저장. 나 다음은 너라는 정보

a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c

head = a
while head: # head가 None이면 꺼버림
    print(head.value)
    head = head.next