# import sys
# sys.stdin = open('5185_이진수.txt')

# T = int(input())
# for test_case in range(1, T+1):
#     # N은 자릿수, oc_str은 16진수
#     N, oct_str = input().split()
#     result = ''
#     for ch in oct_str:
#         to10_num = int(ch, 16)
#         result += format(to10_num, '04b')

#     print(f'#{test_case} {result}')


import sys
sys.stdin = open('5185_이진수.txt')

T = int(input())
for test_case in range(1, T+1):
    N, oct_str = map(str, input().split())
    result = ''
    for i in range(len(oct_str)):
        to_10 = int(oct_str[i], 16)
        to_2 = format(to_10, '04b')
        result = result + to_2

    print(f'#{test_case} {result}')


# 3
# 4 47FE
# 5 79E12
# 8 41DA16CD

# #1 0100011111111110
# #2 01111001111000010010
# #3 01000001110110100001011011001101