import sys
input = sys.stdin.readline
import heapq
T = int(input())
for _ in range(T):

    minH, maxH = [], []
    K = int(input())
    count, cnt = {}, 0
    for i in range(K):
        Q = input().rstrip().split()
        n = int(Q[1])
        if Q[0] == 'I':
            heapq.heappush(minH, n)
            heapq.heappush(maxH, -n)
            count[n] = 1 if n not in count.keys() else count[n]+1
            cnt += 1
        else:
            if cnt == 0:
                continue
            while minH and maxH:
                num = heapq.heappop(minH if n == -1 else maxH)
                num = num if n == -1 else -num
                if count[num] > 0:
                    count[num] -= 1
                    break
            cnt -= 1

    if cnt == 0:
        print("EMPTY")
    else:
        ans1, ans2 = 0, 0
        while maxH:
            ans1 = heapq.heappop(maxH)
            if count[-ans1] > 0:
                break
        while minH:
            ans2 = heapq.heappop(minH)
            if count[ans2] > 0:
                break
        print(-ans1, ans2)
