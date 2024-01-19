import sys
import heapq
input = sys.stdin.readline
import random
N = int(input())
L = []
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(L, (x, y))

length = 0
x, y = heapq.heappop(L)
length, last = y - x, y
while L:
    x, y = heapq.heappop(L)
    if y <= last:
        continue
    elif x <= last < y:
        length += y - last
    else:
        length += y - x
    last = y

print(length)