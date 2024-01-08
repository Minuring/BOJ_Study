V = int(input())
E = int(input())

G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

count , visited = 0, [False for _ in range(V+1)]
def dfs(v):
    global count, G
    visited[v] = True
    count += 1

    for node in G[v]:
        if not visited[node]:
            dfs(node)

dfs(1)
print(count - 1)