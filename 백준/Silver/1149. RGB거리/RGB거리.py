import sys
input = sys.stdin.readline

N = int(input())
L = [[0,0,0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0,0] for _ in range(N+1)]
for i in range(1, N+1):

    dp[i][0] = L[i][0] + min(dp[i-1][1], dp[i-1][2]) # 빨간색, min(이전 초록색, 파란색)
    dp[i][1] = L[i][1] + min(dp[i-1][0], dp[i-1][2]) # 초록색, min(이전 빨간색, 파란색)
    dp[i][2] = L[i][2] + min(dp[i-1][0], dp[i-1][1]) # 파란색, min(이전 빨간색, 초록색)

print(min(dp[N]))