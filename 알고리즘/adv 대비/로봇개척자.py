import sys
sys.sydin = open('전기자동차_충전소.txt')
T = int(input())
for test_case in range(1, T+1):
    # N은 한 변의 길이, M은 동작 가능한 일수 
    N, M = map(int, input().split())
    # 지형 정보
    my_map = [list(map(int, input().split())) for _ in range(N)]
    # 0은 농지, 1은 산. 농지에서 시작. 지형의 테두리는 모두 1 
    # 싹이 나고서 3일 후에 곡식이 열림 
    # 바라보는 방향의 오른쪽, 앞쪽, 왼쪽, 뒤쪽 순으로 이동







    # 구하는 값은 수확 횟수 









#1 4
#2 0
#3 10
#4 11
#5 16
#6 14
#7 20
#8 18
#9 15
#10 22