import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
length, start = 0, -float('inf')
for a, b in lines:

    if start < a:
        start = a
    elif start > b:
        continue
        
    length += abs(b - start)
    start = b

print(length)