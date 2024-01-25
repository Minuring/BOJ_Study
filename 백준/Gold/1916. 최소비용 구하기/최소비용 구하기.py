import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = float('inf')
bus = [[inf for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    bus[s][e] = min(bus[s][e], cost)

# N^2 == 1 000 000
s, e = map(int, input().split())
def dijkstra(s, d):
    visited = [False for _ in range(N+1)]
    dist = [inf for _ in range(N+1)]
    dist[s] = 0

    for _ in range(N-1):
        minDist, minV = inf, 0
        for v in range(1, N+1):
            if not visited[v] and dist[v] < minDist:
                minDist, minV = dist[v], v

        visited[minV] = True
        for v in range(1, N+1):
            if bus[minV][v] != inf and not visited[v] \
                    and dist[v] > dist[minV] + bus[minV][v]:
                dist[v] = dist[minV] + bus[minV][v]
    return dist[d]

print(dijkstra(s, e))