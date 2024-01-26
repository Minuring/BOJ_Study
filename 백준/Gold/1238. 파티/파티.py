import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
road = [[0 for _ in range(N+1)] for _ in range(N+1)]
reverseRoad = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    road[s][e] = cost
    reverseRoad[e][s] = cost

def dijkstra(road, s):
    dist = [float('inf') for _ in range(N+1)]
    dist[s] = 0

    import heapq
    q = [(0, s)]
    while q:
        cost, vertex = heapq.heappop(q)

        for j in range(1, N+1):
            if road[vertex][j] != 0 and dist[j] > dist[vertex] + road[vertex][j]:
                dist[j] = dist[vertex] + road[vertex][j]
                heapq.heappush(q, (dist[j], j))
    return dist

comeback = dijkstra(road, X)[1:]
go = dijkstra(reverseRoad, X)[1:]
ans = max(zip(comeback, go), key=lambda x : sum(x))
print(sum(ans))