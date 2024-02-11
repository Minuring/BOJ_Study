import sys
input = sys.stdin.readline
def dijkstra():
    deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
    import heapq
    dist = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
    dist[0][0] = [1, 1]
    hq = [(1, 0, 0, 0)]

    while hq:
        d, y, x, broken = heapq.heappop(hq)
        # print(d,y,x,broken)

        for dy, dx in zip(deltaY, deltaX):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if broken == 0 and world[ny][nx] == 1 and \
                        dist[ny][nx][1] > dist[y][x][0] + 1:
                    dist[ny][nx][1] = dist[y][x][0] + 1
                    heapq.heappush(hq, (dist[ny][nx][1], ny, nx, 1))

                if world[ny][nx] == 0 and dist[ny][nx][broken] > dist[y][x][broken] + 1:
                    dist[ny][nx][broken] = dist[y][x][broken] + 1
                    heapq.heappush(hq, (dist[ny][nx][broken], ny, nx, broken))

    # print('\n'.join(map(str, dist)))
    return dist[N-1][M-1]

N, M = map(int, input().split())
world = [list(map(int, input().rstrip())) for _ in range(N)]
ans = min(dijkstra())
print(-1 if ans == float('inf') else ans)