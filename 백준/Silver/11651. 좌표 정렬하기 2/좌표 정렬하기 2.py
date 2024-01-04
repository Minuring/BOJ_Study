import sys;input=sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

points.sort(key=lambda p : (p[1],p[0]))
for i in range(n):
    print(points[i][0], points[i][1])