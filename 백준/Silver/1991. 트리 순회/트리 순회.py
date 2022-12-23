num = int(input())

class Node:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

def pre_order(node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left !='.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

tree = {}
for i in range(num):
    data, left, right = input().split(" ")
    tree[data] = Node(left, right, data)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
