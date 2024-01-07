import sys;input=sys.stdin.readline

K = int(input())

L = []
for _ in range(K):

    n = int(input())
    if n == 0:
        L.pop()
    else:
        L.append(n)
print(sum(L))