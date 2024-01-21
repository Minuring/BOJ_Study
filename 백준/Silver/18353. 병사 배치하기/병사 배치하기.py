import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int , input().split()))
D = [L[0]]

def find(D, n):
    lo, hi = -1, len(D)
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if D[mid] <= n:
            hi = mid
        else:
            lo = mid
    return hi

for i in range(1, N):
    n = L[i]

    if n < D[-1]:
        D.append(n)
    else:
        idx = find(D, n)
        D[idx] = n
print(N - len(D))