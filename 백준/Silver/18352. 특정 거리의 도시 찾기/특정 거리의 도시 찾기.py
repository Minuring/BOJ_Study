import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

def dijkstra(s):
    dist = [float('inf') for _ in range(N+1)]
    q = [(0, s)]
    dist[s] = 0

    import heapq
    while q:
        d, v = heapq.heappop(q)

        for next in G[v]:
            if dist[next] > dist[v] + 1:
                dist[next] = dist[v] + 1
                heapq.heappush(q, (dist[next], next))
    return dist

result = dijkstra(X)
ans = [i for i, x in enumerate(result) if x == K]
print('\n'.join(map(str, ans)) if ans else -1)