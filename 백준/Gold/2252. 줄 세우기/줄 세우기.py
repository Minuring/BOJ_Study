import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for i in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

from collections import deque
q = deque()
for stud in range(1, N+1):
    if indegree[stud] == 0:
        q.append(stud)

ans = []
while q:
    stud = q.popleft()
    ans.append(stud)
    for next in G[stud]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(*ans)