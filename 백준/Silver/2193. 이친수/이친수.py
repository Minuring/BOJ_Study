dp = [[0,0] for _ in range(90)]
dp[0] = [0,1]
for i in range(1,90):
    dp[i][0] = dp[i-1][0]
    dp[i][0] += dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[int(input())-1]))