import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, visited):
    for next in range(N):
        if G[i][next] == 1 and not visited[next]:
            visited[next] = 1
            dfs(next, visited)

ans = []
for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i, visited)
    ans.append(visited)

for i in range(N):
    print(*ans[i])