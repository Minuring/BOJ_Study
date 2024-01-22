import sys
input = sys.stdin.readline

from bisect import bisect_left
while True:
    try:
        N = int(input())
        L = list(map(int, input().split()))

        D = [L[0]]
        for i in range(1, N):
            if D[-1] < L[i]:
                D.append(L[i])
            else:
                idx = bisect_left(D, L[i])
                D[idx] = L[i]
        print(len(D))
    except:
        break