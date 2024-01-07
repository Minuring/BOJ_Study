import sys;input=sys.stdin.readline

N, M = map(int, input().split())

numbers = [0] + list(map(int, input().split()))
sumList = [0]*(N+1)
sumList[1] = numbers[1]
for i in range(2,N+1):
    sumList[i] = sumList[i-1] + numbers[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i-1])