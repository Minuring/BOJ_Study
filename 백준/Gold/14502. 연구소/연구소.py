import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
maxCount, zero, wall, virus = 0, -3, 3, 0
for _ in range(N):
    lab.append(list(map(int, input().split())))

deltaY, deltaX = [1, -1, 0, 0], [0, 0, -1, 1]
from collections import deque
import copy
def spread(arr):
    global maxCount, walls

    q = deque([(i, j) for i in range(N) for j in range(M)\
                if arr[i][j] == 2])

    while q:
        y, x = q.popleft()

        for dy, dx in zip(deltaY, deltaX):
            newY, newX = y + dy, x + dx

            if 0 <= newY < N and 0 <= newX < M and \
                    not arr[newY][newX]:

                q.append((newY, newX))
                arr[newY][newX] = 2

    zeroCount = sum([c.count(0) for c in arr])
    if zeroCount > maxCount :
        maxCount = zeroCount


maxCount = 0
from itertools import combinations
wallsCandidates = [(y, x) for y in range(N) for x in range(M) if lab[y][x] == 0]
wallsComb = combinations(wallsCandidates, 3)
for walls in wallsComb:

    arr = copy.deepcopy(lab)
    for y, x in walls:
        arr[y][x] = 1

    spread(arr)

print(maxCount)