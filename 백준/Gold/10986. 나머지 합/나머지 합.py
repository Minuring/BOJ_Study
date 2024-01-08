N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

mods = [0] * (N+1)
counts = [0] * M
for i in range(1,N+1):
    mods[i] = (mods[i-1] + A[i]) % M
    counts[mods[i]] += 1

import math
result = counts[0]
for i in range(M):
    result += math.comb(counts[i], 2)

print(result)