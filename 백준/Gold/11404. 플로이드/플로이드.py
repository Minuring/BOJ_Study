import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    bus[a][b] = min(bus[a][b], cost)
def dijkstra(s):
    visited = [False for _ in range(N+1)]
    dist = [float('inf') for _ in range(N+1)]
    dist[s] = 0

    for _ in range(N-1): #N
        minDist, minV = float('inf'), 0
        for d in range(1, N+1): #N
            if not visited[d] and dist[d] < minDist:
                minDist = dist[d]
                minV = d

        visited[minV] = True
        for dest in range(1, N+1): #N
            if bus[minV][dest] != float('inf') and not visited[dest] \
                    and dist[dest] > dist[minV] + bus[minV][dest]:
                dist[dest] = dist[minV] + bus[minV][dest]

    return [0 if x==float('inf') else x for x in dist]

for s in range(1, N+1):
    print(*dijkstra(s)[1:])
