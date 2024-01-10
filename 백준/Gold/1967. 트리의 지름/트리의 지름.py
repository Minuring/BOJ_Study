import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    G[p].append((c, w))
    G[c].append((p, w))

visited = [False for _ in range(n+1)]
def dfs(v, w):
    visited[v] = True
    greatestVertex, greatestWeight = v, w

    for node, weight in G[v]:
        if not visited[node]:
            dfsV, dfsW = dfs(node, w + weight)
            if dfsW > greatestWeight:
                greatestVertex, greatestWeight = dfsV, dfsW

    return (greatestVertex, greatestWeight)

endV = dfs(1, 0)[0]
visited = [False for _ in range(n+1)]
print(dfs(endV, 0)[1])
