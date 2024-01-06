N = int(input())
cards = list(map(int, input().split()))

from collections import Counter
c = Counter(cards)

M = int(input())
test = list(map(int, input().split()))
for n in test:
    count = c.get(n)
    print(0 if count is None else count, end=' ')