import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
def dfs(i, j):
    global size
    visited[i][j] = True
    size += 1
    for dy, dx in zip(deltaY, deltaX):
        ny, nx = i+dy, j+dx
        if 0 <= ny < M and 0 <= nx < N and paper[ny][nx] == 0 and not visited[ny][nx]:
            dfs(ny, nx)

M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

visited, count = [[False for _ in range(N)] for _ in range(M)], 0
areas = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and not visited[i][j]:
            count += 1
            size = 0
            dfs(i, j)
            areas.append(size)

print(count)
print(*sorted(areas))
