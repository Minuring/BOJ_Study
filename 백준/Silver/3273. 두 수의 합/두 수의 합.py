import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
X = int(input())

L.sort()
l, r, count = 0, len(L)-1, 0
while l < r :
    n = L[l] + L[r]
    if n == X:
        count += 1
        l += 1

    elif n < X:
        l += 1
    elif n > X:
        r -= 1

print(count)