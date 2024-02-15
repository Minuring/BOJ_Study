import sys
input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int, input().split()))
S = int(input())
for _ in range(S):
    gender, number = map(int, input().split())

    if gender == 1:
        n = number
        while n <= N:
            switch[n] = 0 if switch[n] else 1
            n += number
    else:
        l, r = number, number
        maxL, maxR = l, r
        while l >= 1 and r <= N and switch[l] == switch[r]:
            maxL, maxR = l, r
            l -= 1; r += 1

        for i in range(maxL, maxR+1):
            switch[i] = 0 if switch[i] else 1

ans = []
for i in range(1, N+1):
    ans.append(switch[i])
    if i % 20 == 0:
        ans.append("\n")
    else:
        ans.append(" ")
print(*ans, sep='')