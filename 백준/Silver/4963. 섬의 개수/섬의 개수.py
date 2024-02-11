import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

deltaY, deltaX = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
def dfs(i, j):
    visited[i][j] = True
    for dy, dx in zip(deltaY, deltaX):
        ny, nx = i+dy, j+dx
        if 0 <= ny < h and 0 <= nx < w and world[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if world[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)