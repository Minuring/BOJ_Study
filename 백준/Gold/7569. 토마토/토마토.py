import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
for _ in range(H):
    line = []
    for _ in range(N):
        line.append(list(map(int, input().split())))
    tomato.append(line)
#
# for floor in tomato:
#     print('한 개 층')
#     print('\n'.join(map(str, floor)))
#     print()

from collections import deque
q = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                q.append((0, z,y,x))

deltaZ, deltaY, deltaX = [0,0,0,0,-1,1], [-1,1,0,0,0,0], [0,0,-1,1,0,0]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
maxDay = 0

while q:
    day, z, y, x = q.popleft()
    if visited[z][y][x]:
        continue
    visited[z][y][x] = True
    maxDay = max(maxDay, day)

    for dz,dy,dx in zip(deltaZ, deltaY, deltaX):
        nz, ny, nx = z+dz, y+dy, x+dx

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and \
                tomato[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
            tomato[nz][ny][nx] = day + 1
            q.append((day+1, nz, ny, nx))

for floor in tomato:
    if any(0 in x for x in floor):
        print(-1)
        break
else:
    print(maxDay)