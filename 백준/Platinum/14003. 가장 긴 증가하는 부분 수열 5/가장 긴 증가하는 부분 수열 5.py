import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
D = [-float('inf')]
LIS = []

from bisect import *
seq = 0
for n in A:
    if n > D[-1]:
        D.append(n)
        seq += 1
        LIS.append((seq, n))

    else:
        idx = bisect_left(D, n)
        D[idx] = n
        LIS.append((idx, n))
print(seq)
ans = [0]*seq
for i in range(N-1, -1, -1):
    s, n = LIS[i]
    if s == seq:
        seq -= 1
        ans[seq] = n

    if seq == 0:
        break
print(*ans)
