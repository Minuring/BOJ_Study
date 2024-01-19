import sys
input = sys.stdin.readline

N = int(input())
L = list(tuple(map(int, input().split())) for _ in range(N))
D = int(input())

L = sorted([sorted(x) for x in L if abs(x[0] - x[1]) <= D], key=lambda x:x[1])

import heapq
q, maxCount = [], 0
for road in L:
    a, b = road
    if not q:
        heapq.heappush(q, a)
    else:
        while q and q[0] < b - D:
            heapq.heappop(q)
        heapq.heappush(q, a)
    maxCount = max(maxCount, len(q))

print(maxCount)