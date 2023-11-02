def solve(N):
    i = 2
    while i <= N:
        candidates = []
        if i % 3 == 0:
            candidates.append(memo[i//3])
        if i % 2 == 0:
            candidates.append(memo[i//2])
        candidates.append(memo[i-1])
        memo[i] = 1+min(candidates)
        i += 1
    return memo[N]

N = int(input())

memo = [0] * (N+1)
print(solve(N))