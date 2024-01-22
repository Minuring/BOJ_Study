N = int(input())
K = int(input())

lo, hi = 0, K+1
ans = 0
while lo + 1 < hi:
    mid = (lo + hi) // 2

    count = 0
    for i in range(1, N+1):
        count += min(mid // i, N)

    if count >= K:
        hi = mid
        ans = hi
    else:
        lo = mid
print(ans)