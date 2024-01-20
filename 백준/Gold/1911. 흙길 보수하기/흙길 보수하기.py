import sys
input = sys.stdin.readline

N, L = map(int, input().split())
land = sorted([tuple(map(int, input().split())) for _ in range(N)])

place, count = land[0][0], 0
for a, b in land:
    start, end = a, b-1

    if place < start :
        place = start
    elif place > end :
        continue

    size = end - place + 1
    placeCount = size // L + (1 if size % L != 0 else 0)
    place += L * placeCount

    count += placeCount

print(count)