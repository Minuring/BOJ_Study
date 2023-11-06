import sys; input=sys.stdin.readline
V, E = map(int,input().split())

edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x:x[2])

roots = [i for i in range(V+1)]
count = 0
def find(x):
    roots[x] = find(roots[x]) if roots[x]!=x else x
    return roots[x]

for u,v,w in edges:
    uRoot, vRoot = find(u), find(v)
    if uRoot != vRoot :
        count += w

        if uRoot > vRoot :
            roots[uRoot] = v
        else :
            roots[vRoot] = u
print(count)