import sys
input = sys.stdin.readline

wheels = [[]] + [list(map(int, input().rstrip())) for _ in range(4)]
# print('\n'.join(map(str, wheels)))
N, S = 0, 1

def rotateRight(wNum):
    last = wheels[wNum][7]
    for i in range(7, 0, -1):
        wheels[wNum][i] = wheels[wNum][i-1]
    wheels[wNum][0] = last

def rotateLeft(wNum):
    first = wheels[wNum][0]
    for i in range(7):
        wheels[wNum][i] = wheels[wNum][i+1]
    wheels[wNum][7] = first

def check(wNum, direct):
    visited[wNum] = True
    prevLeft, prevRight = wheels[wNum][6], wheels[wNum][2]

    if wNum != 1 and wheels[wNum - 1][2] != prevLeft and not visited[wNum - 1]:
        q.append((wNum-1, direct*-1))
        check(wNum-1, direct*-1)
    if wNum != 4 and wheels[wNum + 1][6] != prevRight and not visited[wNum + 1]:
        q.append((wNum+1, direct*-1))
        check(wNum+1, direct*-1)

K = int(input())
for _ in range(K):
    number, direct = map(int, input().split())

    visited = [False for _ in range(5)]
    q = []
    q.append((number, direct))
    check(number, direct)
    # print(q)
    for n, d in q:
        if d == 1:
            rotateRight(n)
        else:
            rotateLeft(n)

ans = 0
for i in range(4):
    if wheels[i+1][0] == 1:
        ans += 2**i
print(ans)