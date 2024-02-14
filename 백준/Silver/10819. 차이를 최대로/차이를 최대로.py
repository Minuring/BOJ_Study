import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def calc(l):
    result = 0
    for i in range(N-1):
        result += abs(l[i] - l[i+1])
    return result

from itertools import permutations
res = 0
for l in permutations(A):
    res = max(res, calc(l))
print(res)