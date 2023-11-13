def solve_BottomUp(coin, money) :
    dp = [-1]*(money+1)
    dp[0] = 0

    for m in range(1, money+1) :
        dp[m] = float('inf')
        for i in coin:
            if m >= i :
                dp[m] = min(dp[m], 1+dp[m-i])

    return dp[money]

N, K = map(int, input().split())
coin = [0]*N
for i in range(N):
    coin[i] = int(input())

res = solve_BottomUp(coin,K)
print(-1 if res==float('inf') else res)