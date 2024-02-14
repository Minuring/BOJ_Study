import sys
input = sys.stdin.readline

N = int(input())

from itertools import permutations
for l in permutations(range(1, N+1)):
    print(*l)