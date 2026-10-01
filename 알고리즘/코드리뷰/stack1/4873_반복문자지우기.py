import sys
sys.stdin = open('4873_반복문자지우기.txt')

T = int(input())
for test_case in range(1, T+1):
    txt = input()


    stack = []
    for char in txt:
        if stack and char == stack[-1]:
            stack.pop() 
        else:
            stack.append(char)

    result = len(stack)
    print(f'#{test_case} {result}')






    # def delete_char(txt):
    #     # 입력 텍스트를 넣어놓을 스텍
    #     stack = []
    #     # 남길 텍스트
    #     remain_list = []

    #     # 버릴 텍스트
    #     delete_list = []

    #     # txt를 뒤에서부터 읽어서 스택에 넣기
    #     for i in txt[::-1]:
    #         stack.append(i)

    #     # stack이 빌 때까지 반복
    #     while stack:
    #         # 맨 위에 있는 글자 pop
    #         char = stack.pop()
    #         # stack이 비었다면 char를 remain_list에 넣기
    #         if not stack:
    #             remain_list.append(char)
    #         # 만약 char와 stack 맨 위에 있는 글자가 같다면, pop을 한 번 더 해서 두 글자를 없애기
    #         elif char == stack[-1]:
    #             delete_list.append(char)
    #             char2 = stack.pop()
    #             delete_list.append(char2)
    #         # 만약 같지 않다면 char는 remain_list에 push
    #         else:
    #             remain_list.append(char)

    #     # 만약 버릴 텍스트가 없다면 함수 종료
    #     if not delete_list:
    #         return len(remain_list)
    #     # remain_list를 재귀로 반복
    #     return delete_char(remain_list)


    # # remain_list의 길이가 결과
    # result = delete_char(txt)

    # print(f'#{test_case} {result}')


# *return* delete_char(remain_list) 
# return을 적어야함. 출력값이 있어야 함. 안 그러면 None 출력


#3
# ABCCB
# NNNASBBSNV
# UKJWHGGHNFTCRRCTWLALX

#1 1
#2 4
#3 11