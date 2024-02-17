import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

'''
arr.index(max(arr)) 왼쪽에서 LIS, 오른쪽에서 LDS -- 2NlogN
* N개

= N^2 * logN
'''
from bisect import bisect_left
def LIS(L, s, e):
    # list L의 [s,e] 에서 LIS의 길이
    D = [L[s]]
    for i in range(s+1, e+1):
        if L[i] > D[-1]:
            D.append(L[i])
        else:
            idx = bisect_left(D, L[i])
            D[idx] = L[i]
    return len(D)
def LDS(L, s, e):
    # list L의 [s,e] 에서 LDS의 길이
    D = [-L[s]]
    for i in range(s+1, e+1):
        if L[i] < -D[-1]:
            D.append(-L[i])
        else:
            idx = bisect_left(D, -L[i])
            D[idx] = -L[i]
    return len(D)

ans = 0
for i in range(N):
    length = LIS(A, 0, i) + LDS(A, i, N-1) - 1
    ans = max(ans, length)
print(ans)
