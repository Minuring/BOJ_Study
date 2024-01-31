import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

l = 2 * N + 1
pN = 'I' + 'OI' * N
count = 0
for i in range(M - l + 1):
    if S[i:i+l] == pN:
        count += 1
print(count)