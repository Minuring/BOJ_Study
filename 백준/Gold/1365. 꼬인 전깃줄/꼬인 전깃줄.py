import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def find(D, n):
    lo, hi = -1, len(D)
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if D[mid] >= n:
            hi = mid
        else:
            lo = mid
    return hi

D = [A[0]]
for i in range(1, N):
    if D[-1] < A[i]:
        D.append(A[i])
    else:
        idx = find(D, A[i])
        D[idx] = A[i]
print(N - len(D))