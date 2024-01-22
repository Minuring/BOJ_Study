from math import floor
X, Y = map(int, input().split())
Z = floor((Y*100)/X)
# print(Z)

lo, hi = 0, 1000000001
ans = -1
while lo + 1 < hi:
    play = (lo + hi) // 2

    newZ = floor(((Y+play)*100) /(X+play))
    # print(f'{play}판 더 했을 때 newZ = {newZ}')
    if newZ != Z:
        hi = play
        ans = hi
    else:
        lo = play

print(ans)