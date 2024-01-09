import sys;input=sys.stdin.readline

N = int(input())

table = [[] for _ in range(N)]
for y in range(N):
    table[y] = list(map(int, list(input().rstrip())))

from collections import deque
visited = [[False for _ in range(N)] for _ in range(N)]
def bfs(i, j):
    deltaY, deltaX = [1,-1,0,0], [0,0,-1,1]
    q = deque()
    q.append((i,j))
    # (0,0) 에서 count 1로 시작
    count = 0
    while q:
        y, x = q.pop()
        if visited[y][x]:
            continue

        visited[y][x] = True
        count += 1

        for dy, dx in zip(deltaY,deltaX):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N\
                and table[newY][newX] == 1 and not visited[newY][newX]:
                q.append((newY,newX))

    return count

danji = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and not visited[i][j]:
            count = bfs(i, j)
            danji.append(count)

danji.sort()
print(len(danji))
print('\n'.join(map(str, danji)))