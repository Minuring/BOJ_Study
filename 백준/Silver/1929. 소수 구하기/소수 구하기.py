M, N = map(int, input().split())

A = [True for _ in range(1000001)]
A[1] = False

import math
for i in range(2,math.floor(math.sqrt(N)+1)):
    j = i
    while i * j <= N:
        if A[i*j]:
            A[i*j] = False
        j += 1

for i in range(M, N+1):
    if A[i]: print(i)