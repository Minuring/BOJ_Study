import sys
input = sys.stdin.readline

from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
acc = [0] + list(accumulate(A))

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())

    print(acc[j] - acc[i-1])