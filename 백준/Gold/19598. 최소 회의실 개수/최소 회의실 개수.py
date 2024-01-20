import sys
input = sys.stdin.readline

N = int(input())
meetings = sorted([tuple(map(int, input().split())) for _ in range(N)])

import heapq
q = []
for start, end in meetings:
     if q and q[0] <= start:
         heapq.heappop(q)
     heapq.heappush(q, end)

print(len(q))