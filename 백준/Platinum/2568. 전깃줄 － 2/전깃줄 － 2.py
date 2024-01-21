import sys
input = sys.stdin.readline

N = int(input())
L = []
connected_to = {}
for _ in range(N):
    a, b = map(int, input().split())
    L.append((a, b))
    connected_to[b] = a

A = [x[1] for x in sorted(L)]

from bisect import bisect_left
D, check, seq = [A[0]], [(A[0], 1)], 1
for i in range(1, N):
    if D[-1] < A[i]:
        D.append(A[i])
        seq += 1
        check.append((A[i], seq))
    else:
        idx = bisect_left(D, A[i])
        D[idx] = A[i]
        check.append((A[i], idx+1))

ans = []
print(N - len(D))
for i in range(len(check)-1, -1, -1):
    number, sequence = check[i]
    if sequence == seq:
        ans.append(number)
        seq -= 1
    if seq == 0:
        break

removed = [connected_to[x] for x in A if x not in ans]
print(*removed, sep='\n')