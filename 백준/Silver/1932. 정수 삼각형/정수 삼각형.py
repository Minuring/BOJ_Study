import sys
input = sys.stdin.readline

N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

memo = [[-1 for j in range(i+1)] for i in range(N)]
def solve(i, j):
    if i == N:
        return 0
    elif memo[i][j] != -1:
        return memo[i][j]

    left = solve(i+1, j)
    right = solve(i+1, j+1)

    memo[i][j] = max(left, right) + T[i][j]
    return memo[i][j]

print(solve(0, 0))
