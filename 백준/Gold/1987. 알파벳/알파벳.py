import sys
input=sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))

def bfs():
    count = 0
    q = set()
    q.add((0,0,board[0][0]))

    while q:
        y, x, visited = q.pop()
        if len(visited) > count:
            count = len(visited)

        for dy, dx in zip([1,-1,0,0], [0,0,-1,1]):
            ny, nx = y+dy, x+dx

            if 0 <= ny < R and 0 <= nx < C and \
                    board[ny][nx] not in visited:
                q.add((ny, nx, visited + board[ny][nx]))
                
    return count

print(bfs())