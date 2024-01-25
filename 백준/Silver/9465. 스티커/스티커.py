import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = []

    S.append(list(map(int, input().split())))
    S.append(list(map(int, input().split())))

    dp = [[0, 0] for _ in range(N+1)]
    dp[1][0], dp[1][1] = [S[0][0], S[1][0]]
    for i in range(2, N+1):
        dp[i][0] = max(dp[i-1][1] + S[0][i-1], max(dp[i-2]) + S[0][i-1])
        dp[i][1] = max(dp[i-1][0] + S[1][i-1], max(dp[i-2]) + S[1][i-1])

    print(max(dp[N]))