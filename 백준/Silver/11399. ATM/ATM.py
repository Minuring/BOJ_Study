N = int(input())
P = list(map(int, input().split()))

from itertools import accumulate
print(sum(accumulate(sorted(P))))