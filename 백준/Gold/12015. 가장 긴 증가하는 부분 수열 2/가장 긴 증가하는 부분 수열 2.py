import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
def find(n):
    lo, hi, = -1, len(D)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if D[mid] >= n:
            hi = mid
        else:
            lo = mid

    return hi

D = [A[0]]
for i in A[1:]:

    if D[-1] < i:
        D.append(i)
    else:
        idx = find(i)
        D[idx] = i

print(len(D))