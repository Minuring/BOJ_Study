import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
taste = []
for _ in range(N):
    S, B = map(int, input().split())
    taste.append((S, B))

# 1! ~ 10! 합 = 4백만
minDiff = float('inf')
for i in range(1, N+1): # N
    for comb in combinations(taste, i): # << 400만
        S, B = 1, 0
        for s, b in comb:
            S *= s
            B += b

        diff = abs(S - B)
        minDiff = min(minDiff, diff)

print(minDiff)