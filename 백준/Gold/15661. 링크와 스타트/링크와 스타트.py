import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

expectations = [sum(r) + sum(c) for r, c in zip(S, zip(*S))]
teamStatExpectation = sum(expectations) // 2

from itertools import combinations
minDiff = float('inf')
for headCount in range(1, N//2+1):
    for playerStatExpectation in combinations(expectations, headCount):
        minDiff = min(minDiff, abs(teamStatExpectation - sum(playerStatExpectation)))
print(minDiff)