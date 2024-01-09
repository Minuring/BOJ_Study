from collections import deque

M, N = map(int, input().split())
tomatoes = [[0 for _ in range(M)] for _ in range(N)]
cooked, zeroCount = deque(), 0
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(M):
        tomatoes[i][j] = l[j]
        if l[j] == 0:
            zeroCount += 1
        elif l[j] == 1:
            cooked.append((i, j, 0))

def bfs(i, j, day):
    global zeroCount
    #bfs
    deltaY, deltaX = [1,-1,0,0], [0,0,-1,1]

    for dy,dx in zip(deltaY, deltaX):
        newY, newX = i+dy, j+dx

        if N > newY >= 0 and 0 <= newX < M\
                and tomatoes[newY][newX] == 0:
            tomatoes[newY][newX] = day
            cooked.append((newY, newX, day))
            zeroCount -= 1

maxDay = 0
while cooked:
    i, j, day = cooked.popleft()
    maxDay = max(maxDay, day)
    bfs(i, j, day + 1)

if zeroCount != 0:
    print(-1)
else :
    print(maxDay)
