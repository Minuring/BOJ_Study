N = int(input())
L = list(map(int, input().split()))

dp = [0] * N
dp[0] = L[0]

for i in range(1,N):
    if dp[i-1] < 0 < L[i]:
        dp[i] = L[i]

    elif L[i] + dp[i-1] > 0 :
        dp[i] = dp[i-1] + L[i]

    else :
        dp[i] = L[i]

print(max(dp))