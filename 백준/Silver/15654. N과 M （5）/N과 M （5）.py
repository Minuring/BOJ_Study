N, M = map(int, input().split())
nums = list(map(int, input().split()))

from itertools import permutations
for comb in sorted(permutations(nums, M)):
    print(*comb)
