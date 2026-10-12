import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 정수의 개수, M은 빼야하는 숫자 개수
    N, M = map(int, input().split())
    # arr은 숫자 배열. 음수 나올 수 있음.
    arr = list(map(int, input().split()))

    # N-M개를 선택해서 만드는 조합 함수 구현
    r = N-M
    def combination(input_arr, r):
        # 종료 조건
        if r == 0:
            return [[]]

        # 기록할 리스트
        result = []
        # 다음 선택지로 재귀
        for i in range(len(input_arr)):
            pick = input_arr[i]
            next_arr = input_arr[i+1:]
            for next_com in combination(next_arr, r-1):
                result.append([pick] + next_com)

        return result

    # 조합 리스트 만들기
    comb_list = combination(arr, r)

    # 확인용 출력
    # print(comb_list)

    # 최댓값은 마이너스 무한대로 설정하고 시작
    max_cal = float('-inf')

    # 조합 리스트에서 i번째 조합 선택
    for i in range(len(comb_list)):
        # 0번째 인덱스 값에서
        cal = comb_list[i][0]
        # r=1이라면 for문이 돌지 않아서 0번째 인덱스 값이 cal로 남음.
        for j in range(1, r):
            # 홀수 인덱스 값은 더하기
            if j % 2 == 1:
                cal += comb_list[i][j]
            # 짝수 인덱스 값은 빼기
            elif j % 2 == 0:
                cal -= comb_list[i][j]

        max_cal = max(max_cal, cal)

    print(f'#{test_case} {max_cal}')

