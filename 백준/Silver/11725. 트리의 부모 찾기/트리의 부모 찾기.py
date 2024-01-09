import sys;
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

N = int(input())
linkTo = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    linkTo[v1].append(v2)
    linkTo[v2].append(v1)

# print('\n'.join(map(str,linkTo[1:])))
parent = [0 for _ in range(N + 1)]
parent[1] = 1


def dfs(p):
    for v in linkTo[p]:
        if parent[v] == 0:
            parent[v] = p
            dfs(v)


for u in range(1, N + 1):
    dfs(u)

print('\n'.join(map(str, parent[2:])))
