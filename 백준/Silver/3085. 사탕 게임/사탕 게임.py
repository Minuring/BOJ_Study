def longest(row):
    count = 1
    maxCount = 1
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 1
    return maxCount


n = int(input())
board = [[ch for ch in input()] for _ in range(n)]

maxLen = 0
for y in range(n):
    for x in range(n):
        if x < n - 1 and board[y][x] != board[y][x + 1]:
            # 가로 교환
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            for i in range(n):
                maxLen = max(maxLen, longest(board[i]))
                maxLen = max(maxLen, longest([row[i] for row in board]))
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]

        if y < n - 1 and board[y][x] != board[y + 1][x]:
            # 세로 교환
            board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
            for i in range(n):
                maxLen = max(maxLen, longest(board[i]))
                maxLen = max(maxLen, longest([row[i] for row in board]))
            board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]

print(maxLen)