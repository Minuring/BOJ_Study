import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
if N == 1:
    print(1)
else:
    dp[1], dp[2] = 1, 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    print(dp[N] % 15746)
'''
N = 1 : 1
N = 2 : 00 11
N = 3 : 100 001 111
'''