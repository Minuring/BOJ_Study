# 1 2 4 = 1 3 7
# 1 4 2 =
import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]

import heapq
heapq.heapify(cards)
count = 0
while len(cards) > 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    heapq.heappush(cards, A+B)
    count += A+B

print(count)