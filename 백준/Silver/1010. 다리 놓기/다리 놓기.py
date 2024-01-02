import math

T = int(input())

while T > 0:
    T -= 1

    N, M = map(int, input().split())
    print(math.comb(M,N))
