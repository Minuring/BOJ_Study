import heapq,sys; input=sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int,input().split())
    G[u].append([v,w]) #u,v,w

dist = [float('inf') for _ in range(V+1)]
def dijkstra(s):
    hq = []
    heapq.heappush(hq, [0,s])
    dist[s] = 0

    while hq:
        min_dist, min_vertex = heapq.heappop(hq)

        if dist[min_vertex] < min_dist :
            continue

        for v,w in G[min_vertex]:
            if dist[v] > dist[min_vertex]+w:
                dist[v] = dist[min_vertex]+w
                heapq.heappush(hq,[dist[min_vertex]+w,v])

dijkstra(start)
for i in dist[1:]:
    if i == float('inf') :
        print("INF")
    else :
        print(i)

