import sys
input = sys.stdin.readline

from collections import OrderedDict
N = int(input())
switches = list(map(int, input().split()))
lights = list(map(int, input().split()))

A = dict(zip(switches, range(1,N+1)))

# 고려하는 수열은 [인덱스 수열]
# 전구 4,5,1,3,2 순으로 매핑되는 스위치의 [인덱스 수열] 에서 LIS

from bisect import bisect_left
LIS = [A[lights[0]]]
dp, seq = [(1, lights[0])], 1
for i in range(1, N):
    # print(f'{LIS} vs {A[lights[i]]} ', end='')
    if LIS[-1] < A[lights[i]]:
        LIS.append(A[lights[i]])
        # print(f'Appended {A[lights[i]]}')

        seq += 1
        dp.append((seq, lights[i]))
    else:
        idx = bisect_left(LIS, A[lights[i]])
        LIS[idx] = A[lights[i]]
        # print(f'Replaced LIS[{idx}] = {A[lights[i]]}')

        dp.append((idx + 1, lights[i]))

print(seq)
ans = []
for i in range(N-1, -1, -1):
    if dp[i][0] == seq:
        ans.append(dp[i][1])
        seq -= 1
print(*sorted(ans))