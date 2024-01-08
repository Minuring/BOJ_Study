import sys

sys.setrecursionlimit(10000000)
def dfs(v):
    global visited
    visited[v] = True
    for node in G[v]:
        if not visited[node]:
            dfs(node)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0 for _ in range(M)] for _ in range(N)]
    # 가로M 세로N 정점개수K
    for __ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    G = [[] for _ in range(N * M)]
    # 그래프로 변환
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 0: continue
            G[M * i + j].append(M * i + j)

            if i != 0 and farm[i - 1][j] == 1:
                G[M * i + j].append(M * (i - 1) + j)
            if i != N - 1 and farm[i + 1][j] == 1:
                G[M * i + j].append(M * (i + 1) + j)
            if j != 0 and farm[i][j - 1] == 1:
                G[M * i + j].append(M * i + (j - 1))
            if j != M - 1 and farm[i][j + 1] == 1:
                G[M * i + j].append(M * i + (j + 1))

    # 부분 그래프의 개수
    count = 0
    visited = [False for _ in range(N * M)]
    for i in range(N * M):
        if G[i] and not visited[i]:
            dfs(i)
            count += 1

    print(count)
