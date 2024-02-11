import sys
input = sys.stdin.readline

def dijkstra(si, sj, l):
    import heapq
    deltaY, deltaX = [-2,-2,-1,-1,1,1,2,2], [-1,1,-2,2,-2,2,-1,1]
    dist = [[float('inf') for _ in range(l)] for _ in range(l)]
    dist[si][sj] = 0

    hq = [(0, si, sj)]
    while hq:
        d, y, x = heapq.heappop(hq)

        for dy, dx in zip(deltaY, deltaX):
            ny, nx = y + dy, x + dx
            if 0 <= ny < l and 0 <= nx < l and dist[ny][nx] > dist[y][x] + 1:
                dist[ny][nx] = dist[y][x] + 1
                heapq.heappush(hq, (dist[ny][nx], ny, nx))

    return dist

T = int(input())
for _ in range(T):
    l = int(input())
    nowR, nowC = map(int, input().split())
    destR, destC = map(int, input().split())

    dist = dijkstra(nowR, nowC, l)[destR][destC]
    print(dist)