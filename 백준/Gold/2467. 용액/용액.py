import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

lo, hi = 0, N-1
ans, left, right = float('inf'), lo, hi
while lo < hi:

    value = L[lo] + L[hi]
    diff = abs(value)

    if ans > diff:
        ans = diff
        left, right = L[lo], L[hi],

    if value < 0:
        lo += 1
    else:
        hi -= 1
print(left, right)
