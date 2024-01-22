import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
L.sort()
def search(L):
    lo, hi = 0, N-1
    ans, one, two = float('inf'), lo, hi
    while lo < hi:
        value = L[lo] + L[hi]

        if abs(value) < ans:
            ans = abs(value)
            one, two = lo, hi

        if value < 0:
            lo += 1
        else:
            hi -= 1

    print(*sorted([L[one], L[two]]))
search(L)