import sys
input = sys.stdin.readline

N, X = map(int, input().split())
L = [0] + list(map(int, input().split()))
from itertools import accumulate
L = list(accumulate(L))
ans, time = 0, 0
for i in range(N+1-X):
    visit = L[i+X] - L[i]
    if visit > ans:
        ans = visit
        time = 1
    elif visit == ans:
        time += 1

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(time)