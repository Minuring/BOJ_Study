import sys
input=sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
while coins and K > 0:
    coin = coins.pop()
    if K >= coin:
        amount = K // coin

        count += amount
        K = K % coin
print(count)