import sys
input = sys.stdin.readline

N = int(input())

tmp = [False, False] + [True for _ in range(N-1)]
for i in range(2, int(N**(1/2)) + 1):
    if tmp[i]:
        for j in range(i*2, N+1, i):
            tmp[j] = False

L = [i for i, x in enumerate(tmp) if x]
from itertools import accumulate
L = [0] + list(accumulate(L))

l = r = len(L) - 1
count = 0
while l >= 0 and r < len(L):
    n = L[r] - L[l]

    if n == N:
        count += 1
        l -= 1
    elif n < N:
        l -= 1
    else :
        r -= 1

print(count)