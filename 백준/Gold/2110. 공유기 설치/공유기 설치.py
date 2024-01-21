import sys
input = sys.stdin.readline

N, C = map(int, input().split())
H = sorted([int(input()) for _ in range(N)])

low, high, maxDist = 1, H[-1] - H[0], 0
while low <= high:
    dist = (low + high) // 2

    tmp = [H[0]]
    count = 1
    for h in H[1:]:
        if h >= tmp[-1] + dist:
            count += 1
            prev = h
            tmp.append(h)

    if count >= C:
        low = dist + 1
        maxDist = max(dist, maxDist)
    else:
        high = dist - 1
print(maxDist)