import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # A와 B는 16진수. 둘은 길이가 같다.
    A, B = map(str, input().split())

    # 16진수 A를 2진수로 변환하기
    A_result = ''
    for ch in A:
        # 16진수를 10진수로 변환
        hex_to_ten = int(ch, 16)
        # 10진수를 2진수로 변환. 4자릿수. 빈자리는 0으로 표기.
        ten_to_bin = format(hex_to_ten, '04b')
        A_result += ten_to_bin

    # 16진수 B를 2진수로 변환하기
    B_result = ''
    for ch in B:
        # 16진수를 10진수로 변환
        hex_to_ten = int(ch, 16)
        # 10진수를 2진수로 변환. 4자릿수. 빈자리는 0으로 표기.
        ten_to_bin = format(hex_to_ten, '04b')
        B_result += ten_to_bin

    # 확인용 출력
    # print(f'A: {A_result}, B: {B_result}')

    # 숫자가 다른 갯수 세기
    cnt = 0
    for i in range(len(A_result)):
        # 만약 A와 B의 i번째 수가 다르다면
        if A_result[i] != B_result[i]:
            # 숫자 세기
            cnt += 1

    print(f'#{test_case} {cnt}')