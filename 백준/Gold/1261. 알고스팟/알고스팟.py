import sys
input = sys.stdin.readline


M, N = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]


def solve():
    deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
    dist = [[1e10 for _ in range(M)] for _ in range(N)]
    minCount = float('inf')

    import heapq
    q = [(0,0,0)]
    dist[0][0] = 0

    while q:
        cost, i, j = heapq.heappop(q)
        if cost > minCount:
            continue

        if i == N-1 and j == M-1:
            minCount = min(minCount, cost)

        for dy, dx in zip(deltaY, deltaX):
            ny, nx = i+dy, j+dx
            if 0 <= ny < N and 0 <= nx < M and\
                dist[ny][nx] > cost + miro[ny][nx]:
                dist[ny][nx] = cost + miro[ny][nx]
                heapq.heappush(q, (cost + miro[ny][nx], ny, nx))

    return minCount

print(solve())