import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

N = int(input())
height = []
for _ in range(N):
    height.append(list(map(int, input().split())))

def dfs(i, j, rainAmount):
    visited[i][j] = True
    for dy, dx in zip([1,-1,0,0], [0,0,-1,1]):
        ny, nx = i + dy, j + dx

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]\
                and height[ny][nx] > rainAmount:
            dfs(ny, nx, rainAmount)

    return True


maxSafezoneCount = 1
# 비가 오지 않으면 안전 영역의 개수는 1
for rainAmount in range(1, 101):

    visited = [[False for _ in range(N)] for _ in range(N)]
    safezoneCount = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and height[i][j] > rainAmount:
                safezoneCount += 1
                dfs(i, j, rainAmount)

    maxSafezoneCount = max(maxSafezoneCount, safezoneCount)

print(maxSafezoneCount)