import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

i, count, tmp = 0, 0, 0
while i <= M - 3:
    if S[i:i+3] == 'IOI':
        tmp += 1
        i += 2
        if tmp == N:
            count += 1
            tmp -= 1
    else:
        tmp = 0
        i += 1

print(count)