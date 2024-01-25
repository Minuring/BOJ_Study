import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [0 for j in range(K+1)]
dp[0] = 1
for i in range(1, N+1):
    coin = coins[i-1]

    for k in range(coin, K+1):
        dp[k] += dp[k - coin]

print(dp[K])