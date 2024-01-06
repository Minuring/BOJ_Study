
N = int(input())

from collections import deque
cards = deque([i for i in range(N,0,-1)])

while len(cards) > 1:
    cards.pop()
    cards.appendleft(cards.pop())

print(cards.pop())