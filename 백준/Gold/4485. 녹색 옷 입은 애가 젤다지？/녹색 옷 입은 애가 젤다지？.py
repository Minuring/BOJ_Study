import sys
input = sys.stdin.readline

deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
def dijkstra(i, j):
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[i][j] = L[i][j]

    import heapq
    q = [(L[i][j], i, j)]
    while q:
        cost, y, x = heapq.heappop(q)

        for dy, dx in zip(deltaY, deltaX):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and\
                dist[ny][nx] > dist[y][x] + L[ny][nx]:
                dist[ny][nx] = dist[y][x] + L[ny][nx]
                heapq.heappush(q, (dist[ny][nx], ny, nx))

    return dist

seq = 0
while True:
    N = int(input())
    if N == 0:
        break

    seq += 1
    L = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {seq}: {dijkstra(0, 0)[N-1][N-1]}')
