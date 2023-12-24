dp = [0] * 11
dp[:3] = [1,2,4]
def f(n):
    global dp
    if dp[n-1] != 0:
        print(dp[n-1])
        return

    for i in range(3,n):
        if dp[i] != 0 : continue
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n-1])


T = int(input())
for _ in range(T):

    n = int(input())
    f(n)