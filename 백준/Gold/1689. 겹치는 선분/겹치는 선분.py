import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    s, e = map(int, input().split())
    L.append((s, 1))
    L.append((e, -1))

L.sort()

count, maxCount = 0, 0
for location, info in L:

    count += info
    maxCount = max(maxCount , count)
print(maxCount)
