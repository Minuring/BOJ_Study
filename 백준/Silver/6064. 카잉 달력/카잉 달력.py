import sys
input = sys.stdin.readline
T = int(input())
from math import lcm
for _ in range(T):
    M, N, x, y = map(int, input().split())

    ny, count = N if x % N == 0 else x % N, x
    while ny != y:
        ny = (ny + M) % N
        if ny == 0:
            ny = N

        count += M
        if count > lcm(M, N):
            break

    print(-1 if count > lcm(M, N) else count)