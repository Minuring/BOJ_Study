import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
l = [(i+1, *map(int, input().split())) for i, _ in enumerate(range(N))]
l.sort(key=lambda x:x[1])

parent = [i for i in range(N+1)]
def union(a, b):
    parentA = find(a)
    parentB = find(b)
    parent[parentB] = parentA
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

nowN, nowS, nowE = l[0][0], l[0][1], l[0][2]
for info in l[1:]:
    nextN, x1, x2, y = info

    if nowS <= x1 <= nowE:
        union(nowN, nextN)

        if x2 > nowE:
            nowE = x2

    else:
        nowN, nowS, nowE = nextN, x1, x2


for _ in range(Q):
    a, b = map(int, input().split())

    print(1 if find(a)==find(b) else 0)