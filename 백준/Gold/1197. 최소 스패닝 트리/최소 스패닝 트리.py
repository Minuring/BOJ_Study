import heapq
V, E = map(int, input().split()) #정점 수, 간선 수
G = [[] for _ in range(V+1)]
for _ in range(E) :
  u, v, w = map(int, input().split())
  G[u].append([v, w])
  G[v].append([u, w])

sum = 0
visited = [False] * (V+1)

heap = [[0,1]]
count = 0

while heap :
    if count == V : break

    w,u = heapq.heappop(heap)
    if visited[u] : continue

    visited[u] = True
    sum += w
    count += 1

    # u에서 인접한 정점 탐색
    for v,wt in G[u] :
        heapq.heappush(heap, [wt,v])

print(sum)