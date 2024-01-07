import sys;input=sys.stdin.readline

N, M = map(int, input().split())

table = [[] for i in range(N+1)]
for i in range(1,N+1):
    table[i] = [0] + list(map(int, input().split()))

sumTable = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1, N+1):
        sumTable[i][j] = sumTable[i-1][j] + sumTable[i][j-1] \
                         - sumTable[i-1][j-1] + table[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # result = sumTable[y2][x2] - sumTable[y1-1][x2] \
    #     - sumTable[y2][x1-1] + sumTable[y1-1][x1-1]
    result = sumTable[x2][y2] - sumTable[x1-1][y2] \
        - sumTable[x2][y1-1] + sumTable[x1-1][y1-1]
    print(result)