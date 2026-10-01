# def evaluate_postfix(input):
#     txt = input.split()
#     stack = []

#     for token in txt:
#         if token.isdigit():
#             stack.append(int(token))

#         else: 
#             if len(stack) < 2:
#                 return "숫자가 부족합니다"
            
#             right = stack.pop()
#             left = stack.pop()

#             if token == '+':
#                 stack.append(left + right)

#             if token == "-":
#                 stack.append(left - right)

#             if token == "*":
#                 stack.append(left * right)

#             if token == "/":
#                 stack.append(int(left / right))

#     return stack.pop()

# postfix = "100 20 /"

# print(evaluate_postfix(postfix))

# def infix_to_postfix(input):
#     precedence = {
#         '+': 1,
#         '-': 1,
#         '*': 2,
#         '/': 2,
#         '(': 0,
#     }

#     stack = []
#     result = []

#     for token in input:
#         if token.isalnum():
#             result.append(token)

#         elif token == '(':
#             stack.append(token)

#         elif token == ')':
#             while stack and stack[-1] != '(':
#                 result.append(stack.pop())
#             stack.pop()

#         else: 
#             while stack and precedence[stack[-1]] >= precedence[token]:
#                 result.append(stack.pop())
#             stack.append(token)

#     while stack:
#         result.append(stack.pop())

#     return ' '.join(result)

# expr1 = '(2+3)*4'
# expr2 = '2+3*4-5'
# print(infix_to_postfix(expr1))
# print(infix_to_postfix(expr2))

# print(evaluate_postfix(infix_to_postfix(expr1)))

import sys
sys.stdin = open('4874-Forth.txt')
T = int(input())
for test_case in range(1, T+1):
    txt = input().split()
    stack = []
    rlgh = "+-*/"
    result = None

    for token in txt:
        if token.isdigit():
            stack.append(int(token))

        elif token in rlgh:
            if len(stack) < 2:
                result = "error"
                break # for token 

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left+right)
            if token == "-":
                stack.append(left-right)
            if token == "*":
                stack.append(left*right)
            if token == "/":
                stack.append((left//right))       

        elif token == '.':

            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
            break # for token
            

    print(f'#{test_case} {result}')