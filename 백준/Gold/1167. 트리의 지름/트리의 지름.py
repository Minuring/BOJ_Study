import sys
input = sys.stdin.readline

V = int(input())
G = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, input().split()))

    vertex = data[0]
    for i in range(1, len(data)-1, 2):
        v, w = data[i], data[i+1]
        G[vertex].append((v,w))

# print('\n'.join(map(str, G[1:])))

visited = [False for _ in range(V+1)]
farthest = [0, 0]
def dfs(v, w):
    global farthest
    visited[v] = True
    # print(f'{v}방문, w = {w}', end=' || ')

    recursionEnd = True
    for nextV, weight in G[v]:
        if not visited[nextV]:
            recursionEnd = False
            dfs(nextV, w+weight)

    if recursionEnd and w > farthest[1]:
        farthest = [v, w]

dfs(2, 0)

farthest[1], visited = 0, [False for _ in range(V+1)]
dfs(farthest[0], 0)

print(farthest[1])