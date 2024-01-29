import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    n = int(input())
    if n == 0:
        print(0 if not q else heapq.heappop(q))
    else:
        heapq.heappush(q, n)