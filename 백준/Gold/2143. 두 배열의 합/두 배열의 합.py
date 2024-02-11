import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

from itertools import accumulate
accA = [0] + list(accumulate(A))
accB = [0] + list(accumulate(B))

dic = dict()
for i in range(1, N+1):
    for j in range(i, N+1):
        s = accA[j] - accA[i-1]
        # print(f'sum([{i}:{j}+1]) : {s}')
        dic[s] = dic[s] + 1 if s in dic.keys() else 1

count = 0
for i in range(1,M+1):
    for j in range(i, M+1):
        s = accB[j] - accB[i-1]
        if T-s in dic.keys():
            # print(f'B[{i}:{j+1}] sum = {s}, dic[{T-s}] = {dic[T-s]}')
            count += dic[T - s]

print(count)