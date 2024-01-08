N, M, V = map(int, input().split())

G = [[0 for i in range(N+1)] for j in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v], G[v][u] = 1, 1

visited = [False] * (N+1)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1,N+1):
        if G[v][i] != 0 and not visited[i]:
            dfs(i)


dfs(V)
print()
from collections import deque
def bfs(v):
    q, visited = deque(), [False for _ in range(N+1)]
    q.append(v)
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for i in range(1, N+1):
                if G[v][i] != 0 and not visited[i]:
                    q.append(i)


bfs(V)
# print('\n'.join(map(str,G)))