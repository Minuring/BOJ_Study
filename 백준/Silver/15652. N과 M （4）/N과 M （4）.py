from itertools import combinations_with_replacement

N, M = map(int, input().split())

for nums in combinations_with_replacement(range(1, N+1), M):
    for n in nums:
        print(n, end=' ')
    print()