import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = {}
for _ in range(N):
    row = list(map(int, input().split()))
    for i in row:
        if i not in heights:
            heights[i] = 1
        else:
            heights[i] += 1

ansTime, ansHeight = float('inf'), 0
for targetH in range(257):

    time = 0
    block = B
    for h in heights.keys():
        if h == targetH:
            continue

        if h > targetH:
            block += (h - targetH) * heights[h]
            time += (h - targetH) * heights[h] * 2
        else:
            block -= (targetH - h) * heights[h]
            time += (targetH - h) * heights[h]

        if time > ansTime:
            break

    if block >= 0 and time <= ansTime:
        ansTime = time
        ansHeight = targetH
    # print(f'targetH = {targetH} 로 만드는 시간 {time}')

print(ansTime, ansHeight)