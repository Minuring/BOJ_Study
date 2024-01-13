from itertools import permutations
N, M = map(int, input().split())

for nums in permutations(range(1, N+1), M):
    for n in nums:
        print(n, end=' ')
    print()