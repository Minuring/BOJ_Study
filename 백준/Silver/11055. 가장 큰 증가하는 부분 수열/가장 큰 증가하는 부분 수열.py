N = int(input())
A = list(map(int, input().split()))

memo = [0 for _ in range(N)]
def MIS(s):
    if memo[s] != 0:
        return memo[s]

    sum_ = A[s]
    for next in range(s+1, N):
        if A[next] > A[s]:
            sum_ = max(sum_, A[s] + MIS(next))

    memo[s] = sum_
    return sum_

for i in range(N):
    MIS(i)
print(max(memo))