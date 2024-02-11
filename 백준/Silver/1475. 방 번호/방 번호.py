N = list(map(int, input().rstrip()))
from collections import Counter
c = Counter(N)
tmp = c[9] + c[6]
tmp = tmp//2 + tmp%2
max_ = 0
for i in range(10):
    if i == 6 or i == 9:
        continue
    max_ = max(c[i], max_)
count = max(max_, tmp)
print(count)