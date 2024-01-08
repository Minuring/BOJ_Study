import sys;input=sys.stdin.readline

N, M = map(int, input().split())

miro = []
for _ in range(N):
    miro.append([int(x) for x in input().rstrip()])
# 가로N 세로M


G = [[] for _ in range(N * M)]
# 그래프로 변환
for i in range(N):
    for j in range(M):
        if miro[i][j] == 0: continue
        # G[M * i + j].append(M * i + j)

        if i != 0 and miro[i - 1][j] == 1:
            G[M * i + j].append(M * (i - 1) + j)
        if i != N - 1 and miro[i + 1][j] == 1:
            G[M * i + j].append(M * (i + 1) + j)
        if j != 0 and miro[i][j - 1] == 1:
            G[M * i + j].append(M * i + (j - 1))
        if j != M - 1 and miro[i][j + 1] == 1:
            G[M * i + j].append(M * i + (j + 1))


dist = [float('inf') for _ in range(N * M)]
visited = [False for _ in range(N*M)]
def dijkstra(start):
    global dist,visited
    dist[start] = 1

    for i in range(N*M):
        minDist, minVertex = float('inf'), 0
        for j in range(N*M):
            if not visited[j] and dist[j] < minDist:
                minVertex = j
                minDist = dist[j]

        dist[minVertex] = minDist
        visited[minVertex] = True

        if minVertex == N*M - 1:
            break

        for connected in G[minVertex]:
            if not visited[connected] and dist[connected] > dist[minVertex] + 1:
                dist[connected] = dist[minVertex] + 1

dijkstra(0)
print(dist[N*M-1])