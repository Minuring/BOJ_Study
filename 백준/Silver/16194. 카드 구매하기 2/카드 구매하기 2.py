N = int(input())
P = list(map(int, input().split()))

P = [(i+1, v) for i, v in enumerate(P)]

dp = [float('inf')]*(N+1)
dp[0] = 0

for i in range(1,len(P)+1):
    n,p = P[i-1] #n개카드, 팩당가격

    for j in range(n,N+1):
        dp[j] = min( dp[j], dp[j-n]+p )

print(dp[N])