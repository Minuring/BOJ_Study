import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:(x[1],x[0]))

reverses = [x for x in l if x[0] > x[1]]
# 역방향
now, nowDest = reverses[0]
reverseDist = 0
for r in reverses:
    s, e = r

    # 역방향 = s > e
    # e가 nowDest보다 항상 크거나같음.
    # == s >= now, e > nowDest
    if e > now :
        reverseDist += (now - nowDest) * 2
        now, nowDest = s, e

    else: #e <= now
        now = max(now, s)
    # print(f'now={now}, nowDest={nowDest}  돌아가야함')

reverseDist += (now - nowDest) * 2
print(reverseDist + M)