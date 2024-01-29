N, K = map(int, input().split())

def dijkstra(s):
    dist = [float('inf') for _ in range(100001)]
    dist[s] = 0

    import heapq
    q = [(0, s)]
    while q:
        cost, now = heapq.heappop(q)
        for nx in [now*2, now+1, now-1]:
            if 0 <= nx <= 100000 and dist[nx] > dist[now] + 1:
                dist[nx] = dist[now] + 1
                heapq.heappush(q, (dist[nx], nx))

    print(dist[K])
dijkstra(N)