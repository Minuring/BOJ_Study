N, M = map(int, input().split())

def solve(i, L):
    if i == M:
        print(' '.join(map(str, L)))
        return

    for n in range(1, N+1):
        if n not in L:
            solve(i+1, L + [n])

solve(0, [])