import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = []
si, sj = 0, 0
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    for j in range(M):
        if row[j] == 2:
            si, sj = i, j
def bfs(i, j):
    from collections import deque
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]
    dist[i][j] = 0

    deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
    q, visited = deque(), [[False for _ in range(M)] for _ in range(N)]
    q.append((0, i, j))
    while q:
        d, y, x = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True

        for dy, dx in zip(deltaY, deltaX):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and\
                    G[ny][nx] == 1:
                dist[ny][nx] = d + 1
                q.append((dist[ny][nx], ny, nx))

    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                dist[i][j] = 0
            elif dist[i][j] == float('inf'):
                dist[i][j] = -1

    return dist

print = sys.stdout.write
result = bfs(si, sj)
for row in result:
    print(' '.join(map(str, row)) + '\n')