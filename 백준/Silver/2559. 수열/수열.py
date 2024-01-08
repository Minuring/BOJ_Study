N, K = map(int, input().split())

T = list(map(int, input().split()))


subsetSum = sum([T[x] for x in range(K)])
maxSum = subsetSum
for i in range(N-K):

    subsetSum = subsetSum - T[i] + T[i + K]
    maxSum = max(maxSum, subsetSum)

print(maxSum)