import heapq
import sys

N = int(sys.stdin.readline())
times = []
for _ in range(N) :
    tmp = list(map(int, sys.stdin.readline().split()))
    times.append(tmp)
times.sort()
ans = []
heapq.heappush(ans, times[0][1]) #가장 먼저 시작하는 수업을 넣고 시작

for i in range(1, N) : #첫 수업 제외한 수업의 개수만큼
    if times[i][0] >= ans[0] :
        heapq.heappop(ans)

    heapq.heappush(ans, times[i][1])

print(len(ans))