import sys
input = sys.stdin.readline

N, E = map(int, input().split())
edges = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a][b] = c
    edges[b][a] = c
v1, v2 = map(int, input().split())

def dijkstra(s):
    dist = [float('inf') for _ in range(N+1)]
    dist[s] = 0

    import heapq
    q = [(0, s)]

    while q:
        cost, v = heapq.heappop(q)

        for j in range(1, N+1):
            if edges[v][j] != 0 and dist[j] > dist[v] + edges[v][j]:
                dist[j] = edges[v][j] + dist[v]
                heapq.heappush(q, (dist[j], j))

    return dist

start1 = dijkstra(1)
startV1 = dijkstra(v1)
startV2 = dijkstra(v2)

ans1 = start1[v1] + startV1[v2] + startV2[N]
ans2 = start1[v2] + startV2[v1] + startV1[N]
ans = min(ans1, ans2)
print(ans if ans!=float('inf') else -1)