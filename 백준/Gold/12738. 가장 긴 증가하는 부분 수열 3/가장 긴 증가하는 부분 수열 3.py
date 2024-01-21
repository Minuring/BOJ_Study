import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
from bisect import bisect_left
L = [A[0]]
for i in range(1,N):
    n = A[i]
    if n > L[-1]:
        L.append(n)
    else:
        idx = bisect_left(L, n)
        L[idx] = n

print(len(L))
