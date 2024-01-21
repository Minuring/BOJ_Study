import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))

from bisect import bisect_left
D = [A[1]]
for n in range(2, N+1):
    if D[-1] < A[n]:
        D.append(A[n])
    else:
        idx = bisect_left(D, A[n])
        D[idx] = A[n]

print(len(D))