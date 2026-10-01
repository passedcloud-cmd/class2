import sys
sys.stdin = open('5201-컨테이너운반.txt')

T = int(input())
for test_case in range(1, T+1):
    # 컨테이너 수 N
    # 트럭 수 M
    N, M = map(int, input().split())
    things = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # 화물은 무거운 순으로
    things.sort(reverse=True)
    # 트럭은 가벼운 순으로
    trucks.sort(reverse=True)

    # 적재 무게
    t_weight = 0
    # 컨테이너 개수만큼 순회
    for i in range(len(things)):
        for j in range(len(trucks)):
            # 만약 화물 <= 트럭이라면
            if things[i] <= trucks[j]: 
                # 적재 무게 추가
                t_weight += things[i]
                # 화물을 실은 트럭은 출발~
                trucks.pop(j)
                # 다음 컨테이너로 돌아가기
                break # for i

    # 만약 옮긴 컨테이너가 0개라면
    if t_weight == 0:
        result = 0
    else:
        result = t_weight

    print(f'#{test_case} {result}')