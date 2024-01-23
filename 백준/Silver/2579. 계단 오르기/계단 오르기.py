import sys

input = sys.stdin.readline

N = int(input())
S = [0] + [int(input()) for _ in range(N)]
memo = [[-1, -1] for _ in range(N+1)]

def step(i, contiguous):
    if i < 0 or contiguous == 3:
        return 0
    elif memo[i][contiguous-1] != -1:
        return memo[i][contiguous-1]

    one = step(i-1, contiguous+1)
    two = step(i-2, 1)
    memo[i][contiguous-1] = max(one, two) + S[i]

    return memo[i][contiguous-1]

print(step(N, 1))
