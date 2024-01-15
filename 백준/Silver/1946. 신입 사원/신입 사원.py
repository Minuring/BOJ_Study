import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    L = [tuple(map(int, input().split())) for _ in range(N)]
    
    L.sort()
    cutLineB = L[0][1]

    count = 1
    for i in range(1, len(L)):
        if L[i][1] < cutLineB:
            count += 1
            cutLineB = L[i][1]

    print(count)