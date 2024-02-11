import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

place = [list(map(int, input().split())) for _ in range(N)]
def go(direct = 1):
    global r, c, d
    nr, nc = r, c
    if d == 0: #북
        nr -= direct
    elif d == 1: #동
        nc += direct
    elif d == 2: #남
        nr += direct
    else: #서
        nc -= direct

    r, c = nr, nc

def exists_not_cleared(y, x):
    flag = False
    for dy, dx in zip(deltaY, deltaX):
        ny, nx = r + dy, c + dx
        if place[ny][nx] == 0:
            flag = True
            break

    return flag

deltaY, deltaX = [-1,1,0,0], [0,0,-1,1]
count = 0
while True:
    if place[r][c] == 0:
        place[r][c] = 2
        count += 1

    if not exists_not_cleared(r, c):
        go(direct=-1)
        if place[r][c] == 1:
            break
    else:
        orgR, orgC = r, c
        d = (d + 3) % 4
        go(direct=1)
        if place[r][c] != 0:
            go(direct=-1)

print(count)