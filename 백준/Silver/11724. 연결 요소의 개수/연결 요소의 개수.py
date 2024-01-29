import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
N, M = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1
def dfs(s):
    global visited
    visited[s] = True
    for v in range(1, N+1):
        if G[s][v] != 0 and not visited[v]:
            dfs(v)

count, visited = 0, [False for _ in range(N+1)]
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)