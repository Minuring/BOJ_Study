import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())

M = int(input())
R = [[] for _ in range(N+1)]
for _ in range(M):
    p, c = map(int, input().split())

    R[c].append(p)
    R[p].append(c)
visited, found = [False for _ in range(N+1)], False
def dfs(v, count):
    global b, found
    visited[v] = True
    if v == b:
        print(count)
        found = True
        return

    for next in R[v]:
        if not found and not visited[next]:
            dfs(next, count+1)

dfs(a, 0)
if not found:
    print(-1)