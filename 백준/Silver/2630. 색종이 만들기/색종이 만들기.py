import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
def isOneColor(i1, j1, i2, j2):
    color = L[i1][j1]
    for i in range(i1, i2):
        for j in range(j1, j2):
            if L[i][j] != color:
                return False
    return True

white, blue = 0, 0
def divide(n, i1, j1, i2, j2):
    global white, blue
    if isOneColor(i1, j1, i2, j2) or n == 1:
        if L[i1][j1] == 0:
            white += 1
        else:
            blue += 1
        # print(f'n=={n} 범위 [{i1},{j1}]~({i2},{j2}) 에서 w={white}, b={blue}')

        return

    mid_i = (i1 + i2) // 2
    mid_j = (j1 + j2) // 2

    divide(n//2, i1, j1, mid_i, mid_j)
    divide(n//2, i1, mid_j, mid_i, j2)
    divide(n//2, mid_i, mid_j, i2, j2)
    divide(n//2, mid_i, j1, i2, mid_j)

divide(N, 0,0, N,N)
print(white, blue, sep='\n')