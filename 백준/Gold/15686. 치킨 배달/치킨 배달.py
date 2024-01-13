import sys
input = sys.stdin.readline
N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] == 1:
            houses.append((i,j))
        elif l[j] == 2:
            chickens.append((i,j))

def getChickenDist(i, j, chickens):
    minDist = float('inf')
    for y, x in chickens:
        dist = abs(y-i) + abs(x-j)
        minDist = min(minDist, dist)

    return minDist

from itertools import combinations
minDist = float('inf')
for m in range(1, M+1):

    for survivedChickens in combinations(chickens, m):
        chickenDistSum = 0
        for i, j in houses:
            chickenDistSum += getChickenDist(i, j, list(survivedChickens))
        minDist = min(minDist, chickenDistSum)

print(minDist)