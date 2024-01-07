import sys;input=sys.stdin.readline
n = int(input())
ans = 0

if n != 0:

    l = []
    for i in range(n):
        l.append(int(input()))

    exceptCount = int(0.5 + n * 0.15)
    l.sort()

    ans = int(0.5 + (sum(l[ exceptCount : len(l)-exceptCount ]) / (n - exceptCount*2)))

print(ans)