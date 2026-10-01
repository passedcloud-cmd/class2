# 완전이진트리
N = 6
raw_data = ['A', 'B', 'C', 'D', 'E', 'F']

tree = [0] + raw_data

def get_children(idx):
    if idx >= len(tree):
        return None
    # print(len(tree))
    left_idx = idx * 2
    # print(f'left_idx :{left_idx}')
    if left_idx >= len(tree):
        print(f'{tree[idx]}왼쪽자식 없음')
    else: 
        print(f'{tree[idx]} 왼쪽자식: {tree[left_idx]} / 인덱스: {left_idx}')

    right_idx = idx * 2 + 1
    # print(f'right_idx :{right_idx}')
    if right_idx < len(tree):
        print(f'{tree[idx]} 오른쪽자식: {tree[right_idx]} / 인덱스: {right_idx}')
    else:
        print(f'{tree[idx]}오른쪽자식 없음')

get_children(3)





# 완벽이진트리가 아닌 그냥 이진트리
V = 13 
E = V - 1
edge_input = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
edge = list(map(int, edge_input.split()))

left = [0] * (V+1)
right = [0]* (V+1)

for i in range(E):
    parent = edge[i*2]
    child = edge[i*2+1]

    if left[parent] == 0:
        left[parent] = child
    else: 
        right[parent] = child

print('왼쪽자식 정보:', left)
print('오른쪽자식 정보:', right)




# 전위 순회
def preoder(node):
    if node == 0:
        return None

    print(node, end = ' ')
    preoder(left[node])
    preoder(right[node])

preoder(1)
print('\n')

# 중위 순회
def inorder(node):
    if node == 0:
        return None

    inorder(left[node])
    print(node, end = ' ')
    inorder(right[node])

inorder(1)
print('\n')

# 후위 순회
def postorder(node):
    if node == 0:
        return None

    postorder(left[node])
    postorder(right[node])
    print(node, end = ' ')

postorder(1) 

# 재귀 한계 올려놓기
import sys
sys.setrecursionlimit(10**6)
