import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
indices_in_B = dict(zip(B, range(N)))

from bisect import bisect_left
LIS = [indices_in_B[A[0]]]
for i in range(1, N):
    if LIS[-1] < indices_in_B[A[i]]:
        LIS.append(indices_in_B[A[i]])
    else:
        idx = bisect_left(LIS, indices_in_B[A[i]])
        LIS[idx] = indices_in_B[A[i]]

print(len(LIS))