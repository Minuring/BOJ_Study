import sys
input = sys.stdin.readline

from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break

    K, *S = arr
    for i in combinations(S, 6):
        print(*i)

    print()