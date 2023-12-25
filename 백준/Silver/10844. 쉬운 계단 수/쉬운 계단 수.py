dp = [[0]*10 for _ in range(101)]
dp[1] = [0] + [1 for _ in range(1,10)]
mod = 1000000000

for i in range(2,101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % mod
        elif 1 <= j <= 8:
            dp[i][j] = ( dp[i-1][j-1] + dp[i-1][j+1] ) % mod
        else:
            dp[i][j] = dp[i-1][8] % mod

N = int(input())
print(sum(dp[N]) % mod)
