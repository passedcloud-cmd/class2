import sys
sys.stdin = open("11기-채점시스템만들기.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 학생 수, M은 문항 수
    N, M = map(int, input().split())
    # correct_answer 답안지
    correct_answer = list(map(int, input().split()))
    # arr는 학생들이 작성한 답
    student_answer = [list(map(int, input().split())) for _ in range(N)]

    # 학생들의 점수를 기록한 2차원 리스트 만들기
    total_scores = [[0] * M for _ in range(N)]

    # 학생들의 답안지를 모두 채점
    for n in range(N):
        # 다른 학생의 답안지로 교체할 때마다 점수 리셋
        score = 0
        # 모든 문항수를 순회
        for i in range(M):
            # 정답이라면 해당 문제의 점수 +1
            if correct_answer[i] == student_answer[n][i]:
                score += 1
                # 해당 학생의 점수 기록표 갱신
                total_scores[n][i] = score
            # 정답이 아니라면 점수 0으로 리셋
            else:
                score = 0

    # 각 학생들의 점수 합계 구하기
    max_score = float('-inf') # 임의로 설정
    for n in range(N):
        if sum(total_scores[n]) > max_score:
            max_score = sum(total_scores[n])

    print(f'#{test_case} {max_score}')

# 출력
# #1 15