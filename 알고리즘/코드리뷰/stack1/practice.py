import sys
sys.stdin = open('stack_practice.txt')

T = int(input())

for tc in range(T):
    txt = input()

    # 괄호를 넣을 stack 리스트 만들기
    stack = []
    # 결과값은 -1로 시작
    result = -1
    # txt의 모든 글자를 순회
    # 여는 괄호를 만나면 stack에 넣기. 닫는 괄호를 만나면 stack에서 여는 괄호를 꺼내기. 
    for t in txt:
        # 여는 괄호의 경우
        if t == '(' or t == '[':
            stack.append(t)
        # 닫는 괄호 ')'의 경우
        elif t == ')':
            # 만약 stack이 비어있다면 -1을 반환
            if len(stack) == 0:
                result = -1
                break # for t
            # stack에 뭔가 있다면 pop
            else:
                item = stack.pop()
                # 꺼낸 요소가 '('가 아니라면 -1을 반환
                if item != '(':
                    result = -1
                    break
        # 닫는 괄호 ']'의 경우
        if t == ']':
            # 만약 stack이 비어있다면 -1을 반환
            if len(stack) == 0:
                result = -1
                break # for t
            # stack에 뭔가 있다면 pop
            else:
                item = stack.pop()
                # 꺼낸 요소가 '['가 아니라면 -1을 반환
                if item != '[':
                    result = -1
                    break

    # txt를 모두 순회했는데 stack에 뭐가 남아있으면 -1 반환
    if not len(stack):
        result = 1
    else:
        result = -1


    print(result)

    # txt 개수만큼 반복





# 3
# (12[3]{45}[])
# ([{)]}999
# ([]{})((12345){[67]})

#1 1
#2 -1
#3 1