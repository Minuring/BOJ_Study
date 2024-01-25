import sys
input = sys.stdin.readline

N, M = map(int, input().split())
friends = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a][b] = friends[b][a] = 1

def dijkstra(s):
    import heapq
    dist = [float('inf') for _ in range(N+1)]
    dist[s], q = 0, [(0, s)]

    while q:
        d, minV = heapq.heappop(q)

        for other in range(1, N+1):
            if friends[minV][other] and dist[other] > friends[minV][other] + dist[minV]:
                dist[other] = friends[minV][other] + dist[minV]
                heapq.heappush(q, (dist[other] + 1, other))
    return sum([x for x in dist[1:] if x != float('inf')])

ans, ansN = float('inf'), 0
for i in range(1, N+1):
    result = dijkstra(i)
    if result < ans:
        ans = result
        ansN = i
print(ansN)