import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = {}
for _ in range(N):
    site, pw = input().split()
    L[site] = pw

for _ in range(M):
    print(L[input().rstrip()])