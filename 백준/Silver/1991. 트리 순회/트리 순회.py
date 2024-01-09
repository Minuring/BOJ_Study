import sys;
input = sys.stdin.readline

N = int(input())
nodes = {}
for _ in range(N):
    name, l, r = input().rstrip().split()
    nodes[name] = (l, r)

def preOrder(node):
    if node == '.': return
    left, right = nodes[node]
    print(node, end='')
    preOrder(left)
    preOrder(right)

def inOrder(node):
    if node == '.': return
    left, right = nodes[node]
    inOrder(left)
    print(node, end='')
    inOrder(right)

def postOrder(node):
    if node == '.': return
    left, right = nodes[node]
    postOrder(left)
    postOrder(right)
    print(node, end='')

preOrder('A'); print()
inOrder('A'); print()
postOrder('A');