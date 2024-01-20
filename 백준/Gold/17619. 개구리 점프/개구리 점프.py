import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
bridges = [(i+1, tuple(map(int, input().split()))) for i, _ in enumerate(range(N))]
bridges_sorted_X = sorted(bridges, key=lambda x:x[1][0])
# print(bridges)

visited = [False for _ in range(N+1)]
def jump(now, dest):
    global visited
    nowN, nowX1, nowX2, nowY = now[0], now[1][0], now[1][1], now[1][2]
    # print(f'Jumped now = {now}')
    if nowN == dest:
        return True
    #elif 더이상 점프가능한 곳 없으면 리턴
    visited[nowN] = True
    # 점프 가능한 곳 = y좌표 다르면서 범위 내 있는 다른 통나무
    # O(N)
    candidates = []
    for other in bridges_sorted_X:
        number, x1, x2, y = other[0], other[1][0], other[1][1], other[1][2]
        if number == nowN or y == nowY:
            continue
        elif x2 < nowX1:
            continue
        elif x1 > nowX2:
            break
        elif not visited[number]:
            candidates.append(other)

    if not candidates:
        return False

    # print(candidates)
    under = max(candidates, key=lambda x:x[1][2] and x[1][2] < nowY)
    upper = min(candidates, key=lambda x:x[1][2] and x[1][2] > nowY)
    underY, upperY = under[1][2], upper[1][2]

    candidates = [x for x in candidates if x[1][2] == underY or x[1][2] == upperY]
    # print(underY, upperY, candidates)
    for other in candidates:
        if jump(other, dest):
            return True

    visited[nowN] = False
    return False

for _ in range(Q):
    a, b = map(int, input().split())
    # a -> b ?
    print(1 if jump(bridges[a-1], b) else 0)


