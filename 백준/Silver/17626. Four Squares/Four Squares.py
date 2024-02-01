N = int(input())

dp = [0 for _ in range(N+1)]
dp[1] = 1
for i in range(2, N+1):
    j, minV = 1, float('inf')
    while j**2 <= i:
        minV = min(minV, dp[i - j**2])
        j += 1
    dp[i] = minV + 1

print(dp[N])