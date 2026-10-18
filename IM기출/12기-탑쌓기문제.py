import sys
sys.stdin = open("12기-탑쌓기문제.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 화물 개수
    # W1, W2는 각 탑의 높이
    N, W1, W2 = map(int, input().split())
    # k_arr는 화물별 무게
    arr = list(map(int, input().split()))

    # 내림차순으로 정렬
    arr_sorted = sorted(arr, reverse = T)

    # 층수마다 어떤 화물을 쌓을지 리스트 만들기
    W1_list = []
    W2_list = []

    # 무거운 화물 순으로 탑1과 탑2에 번갈아가면서 넣기
    # 탑 하나가 꽉 차면 나머지 화물은 다른 탑에 몰아넣기
    for i in range(N):
        # 짝수 번째 화물은 탑1에 넣기
        if i % 2 == 0:
            W1_list.append(arr_sorted[i])
            W1 -= 1
            # 만약 W1 탑에 화물이 다 찼다면 나머지 화물은 W2에 다 넣기
            if W1 == 0:
                for j in range(i + 1, N):
                    W2_list.append(arr_sorted[j])
                # 화물 다 넣었으면 break
                break # for i

        # 홀수 번째 화물은 탑2에 넣기
        if i % 2 == 1:
            W2_list.append(arr_sorted[i])
            W2 -= 1
            # 만약 W2 탑에 화물이 다 찼다면 나머지 화물은 W1에 다 넣기
            if W2 == 0:
                for j in range(i + 1, N):
                    W1_list.append(arr_sorted[j])
                # 화물 다 넣었으면 break
                break # for i

    need_fee = 0 # 필요한 비용은 0부터 시작

    # W1 짓는 데 필요한 비용
    for i in range(len(W1_list)):
        need_fee += (i + 1) * W1_list[i]

    # W2 짓는 데 필요한 비용
    for j in range(len(W2_list)):
        need_fee += (j + 1) * W2_list[j]

    print(f'#{test_case} {need_fee}')










# 출력
# #1 22
# #2 30
# #3 30
# #4 126