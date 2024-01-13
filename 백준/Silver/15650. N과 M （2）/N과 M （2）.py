from itertools import combinations
N, M = map(int, input().split())

for nums in combinations(range(1, N+1), M):
    for n in nums:
        print(n, end=' ')
    print()