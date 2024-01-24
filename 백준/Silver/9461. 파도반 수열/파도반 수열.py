import sys
input = sys.stdin.readline

P = [1,1,1]
for i in range(3, 101):
    P.append(P[i-2] + P[i-3])

T = int(input())
for _ in range(T):
    print(P[int(input()) - 1])