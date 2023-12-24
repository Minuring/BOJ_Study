N = int(input())
P = list(map(int, input().split()))

P = [(i+1, v) for i, v in enumerate(P)]
P.sort(key=lambda x : x[1]/x[0] if x[0]!=0 else x[1], reverse=True)

dp = [0]*(N+1)

for i in range(1,len(P)+1):
    n,p = P[i-1] #n개카드, 팩당가격

    for j in range(n,N+1):
        dp[j] = max( dp[j], dp[j-n]+p )

print(dp[N])