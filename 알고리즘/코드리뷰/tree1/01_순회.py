V = 13
E = V - 1
input = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
edge = list(map(int,input.split()))


left = [0] * (V+1)
right = [0] * (V+1)
for i in range(E):
    parent = edge[i*2]
    child = edge[i*2+1]

    if left[parent] == 0:
        left[parent] = child

    else:
        right[parent] = child


# 전위 순회
def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])

print('전위 순회')
preorder(1)
print('\n') # 줄바꿈

# 중위 순회
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

print('중위 순회')
inorder(1)
print('\n') # 줄바꿈

# 후위 순회
def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        print(node, end =' ')

print('후위 순회')
postorder(1)
print('\n') # 줄바꿈