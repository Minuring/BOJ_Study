import sys;

input = sys.stdin.readline

N, M = map(int, input().split())

A = []
A.append([0 for i in range(M + 1)])
for i in range(N):
    A.append([0] + list(map(int, input().split())))

sumArray = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sumArray[i][j] = sumArray[i - 1][j] + sumArray[i][j - 1] - \
                         sumArray[i - 1][j - 1] + A[i][j]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

    result = sumArray[x][y] - sumArray[x][j - 1] - \
             sumArray[i - 1][y] + sumArray[i-1][j-1]

    print(result)