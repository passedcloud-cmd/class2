import sys
sys.stdin= open('1232-사칙연산.txt', 'r')
sys.setrecursionlimit(10**6)

for test_case in range(1, 11):

    # N = 각 케이스의 정점 개수
    N = int(input())

    tree_info = [[] for _ in range(N+1)]
    for _ in range(N):
        node_input = input().split()
        tree_info[int(node_input[0])] = node_input

    # print(tree_info)

    def calc(node_index):
        if len(tree_info[node_index]) == 2:
            return int(tree_info[node_index][1])

        else:
            left_child_idx = int(tree_info[node_index][2])
            right_child_idx = int(tree_info[node_index][3])

            left_val = calc(left_child_idx)
            right_val = calc(right_child_idx)

            # print(f'left_val:{left_val}')
            # print(f'right_val:{right_val}')

            op = tree_info[node_index][1]
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            else:  # '/'
                # 문제 조건에 따라 정수 나눗셈으로 처리
                return left_val // right_val


    result = calc(1)
    print(f"#{test_case} {result}")