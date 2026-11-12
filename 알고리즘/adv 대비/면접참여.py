import sys
sys.stdin = open('면접참여.txt')
T = int(input())
for test_case in range(1, T+1):
    # N은 문제 개수
    # M은 맞힌 개수
    # K는 카운터를 초기화 하는 개수 
    N, M, K = map(int, input().split())

    def make_asers(N, M, K):
        """총점이 가장 작아지도록 O / X 순서를 만들어 반환"""
        wrong = N - M # 틀린 개수
        # X 하나 뒤에는 O를 K -1 개까지 붙여도 2배가 일어나지 않음
        safe = wrong * (K-1)
        # X 뒤에 다 숨기지 못한 O는 맨 앞에 몰아두기 (총점이 작을 때 2배)
        front = max(M - safe, 0)     

        answers = ['O'] * front 
        left = M - front 
        for _ in range(wrong):
            answers.append('X')
            # 남은  O를 k - 1개까지만 붙인다
            add = min(K-)