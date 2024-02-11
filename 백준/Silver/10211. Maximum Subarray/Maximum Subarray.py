import sys
input = sys.stdin.readline

def MSS(accL):
    res = -float('inf')
    for i in range(1,len(accL)):
        for j in range(i, len(accL)):
            res = max(res, accL[j] - accL[i-1])

    return res

from itertools import accumulate
T = int(input())
for _ in range(T):
    N = int(input())
    L = [0] + list(map(int, input().split()))
    L = list(accumulate(L))

    print(MSS(L))
