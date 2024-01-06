T = int(input())

from collections import deque

for _ in range(T):
    n, m = map(int, input().split())

    printer = [i for i in range(1, n+1)]
    priorities = list(map(int, input().split()))
    queue = deque(zip(printer, priorities))

    seq = 0
    while queue:
        maxPriority = max(queue, key=lambda x:x[1])[1]
        curr = queue.popleft()

        if curr[1] == maxPriority:
            seq += 1
            if curr[0] == m + 1:
                print(seq);break
        else:
            queue.append(curr)

