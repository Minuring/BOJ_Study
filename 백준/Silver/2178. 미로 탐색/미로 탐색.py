import sys

input = sys.stdin.readline

N, M = map(int, input().split())

miro = []
for _ in range(N):
    miro.append([int(x) for x in input().rstrip()])
# 가로N 세로M

# bfs
from collections import deque
def bfs():
    deltaY, deltaX = [1, -1, 0, 0], [0, 0, -1, 1]  # 상하좌우
    visited = [[False for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        i, j, dist = queue.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True

        if i == N - 1 and j == M - 1:
            return dist

        for dy, dx in zip(deltaY, deltaX):
            newI, newJ = i + dy, j + dx
            if 0 <= newI < N and 0 <= newJ < M and \
                miro[newI][newJ] == 1 and not visited[newI][newJ]:
                queue.append((newI, newJ, dist + 1))

print(bfs())
