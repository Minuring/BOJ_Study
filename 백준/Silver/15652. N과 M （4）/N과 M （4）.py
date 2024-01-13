N, M = map(int, input().split())

def solve(i, L):
    if i == M:
        print(' '.join(map(str, L)))
        return

    for n in range(1, N+1):
        if not L or L[-1] <= n:
            solve(i+1, L + [n])


solve(0, [])