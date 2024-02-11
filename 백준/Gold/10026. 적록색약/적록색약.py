import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def getCount(grid):
    global visited
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count += 1
                dfs(i, j, grid[i][j])
    return count
def dfs(i, j, color):
    global visited
    visited[i][j] = True
    for dy, dx in zip(deltaY, deltaX):
        ny, nx = i + dy, j + dx
        if 0 <= ny < N and 0 <= nx < N and \
                grid[ny][nx] == color and not visited[ny][nx]:
            dfs(ny, nx, color)


N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]
visited = []
deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]

print(getCount(grid), end=' ')
for i in range(N):
    grid[i] = ['G' if x == 'R' else x for x in grid[i]]
print(getCount(grid))