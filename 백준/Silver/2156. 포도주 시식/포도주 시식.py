import sys
input = sys.stdin.readline

N = int(input())
L = [0] + [int(input()) for _ in range(N)]

if N <= 2:
    print(L[N] + L[N-1])
else:
    dp = [0] * (N+1)
    dp[1], dp[2] = L[1], L[1] + L[2]
    for i in range(3, N+1):

        one = dp[i-3] + L[i-1] + L[i]
        two = dp[i-2] + L[i]
        dp[i] = max(one, two, dp[i-1])

    print(dp[N])