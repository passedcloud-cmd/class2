import sys
sys.stdin = open('1238_Contact.txt')
from collections import deque

for tc in range(1,11):
    # 데이터 길이와 시작점
    data_len, start = map(int, input().split())
    # from, to 쌍이 나열된 데이터
    data = list(map(int, input().split()))

    # 인접 리스트. 번호가 1~100이니까 101까지 준비
    graph = [[] for _ in range(101)]
    for i in range(0, data_len, 2):
        frm = data[i]
        to = data[i+1]
        # 중복 간선 방지: 이미 있는 연결이면 추가 안함
        if to not in graph[frm]:
            graph[frm].append(to)

    # BFS
    visited = [False] * 101
    queue = deque([start])
    visited[start] = True
    last_level = [start] # 마지막 레벨에 속한 사람들 저장

    while queue:
        # 현재 큐에 들어있는 노드 수 = 이번 레벨에서 동시에 사람 수
        level_size = len(queue)
        current_level = [] # 이번 레벨에서 새로 연락 받을 사람들

        # 이번 레벨의 노드 전부 처리
        for _ in range(level_size):
            now = queue.popleft()

            # now가 연락할 수 있는 모든 사람을 확인
            for nxt in graph[now]:
                # 아직 연락받지 않은 사람만 처리
                if not visited[nxt]:
                    visited[nxt] = True # 연락 완료
                    queue.append(nxt) # 다음 레벨 탐색 대상에 추가
                    current_level.append(nxt) # 이번 레벨 기록

        # 이번 레벨에서 새로 연락받은 사람이 있으면 last_level 갱신
        # (비어있으면 갱신하지 않음 => 이전 레벨이 마지막으로 유지)
        if current_level:
            last_level = current_level
                    
    # 마지막 레벨에서 가장 큰 번호 출력
    print(f'#{tc} {max(last_level)}')




#1 17
#2 96
#3 49
#4 39
#5 49
#6 1
#7 28
#8 45
#9 59
#10 64
