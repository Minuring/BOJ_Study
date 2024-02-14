import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]
maxScore = -float('inf')
def put(i, j, count, score):
    global maxScore

    if count == 4:
        # if score > maxScore:print(progress, score)
        maxScore = max(maxScore, score)
    else:
        for dy, dx in zip([1,0,0], [0,-1,1]):
            ny, nx = i+dy, j+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:

                visited[ny][nx] = True

                if count == 2:
                    put(i, j, 3, score+board[ny][nx])
                put(ny, nx, count+1, score+board[ny][nx])

                visited[ny][nx] = False


for y in range(N):
    for x in range(M):
        visited[y][x] = True
        put(y, x, 1, board[y][x])
        visited[y][x] = False

print(maxScore)