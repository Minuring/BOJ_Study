N, K = map(int, input().split())

def bfs(N, K):
    from collections import deque
    visited = [False for _ in range(100001)]
    q = deque()
    q.append([0, N])

    while q:
        cost, x = q.popleft()
        if visited[x]:
            continue
        visited[x] = True

        if x == K:
            return cost

        if x*2 <= 100000:
            q.appendleft([cost, x*2])
        if x+1 <= 100000:
            q.append([cost+1, x+1])
        if x-1 >= 0:
            q.append([cost+1, x-1])

print(bfs(N, K))