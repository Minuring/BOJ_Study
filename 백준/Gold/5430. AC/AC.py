from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    L = input().strip().lstrip('[').rstrip(']')

    q = deque() if not L else deque(list(map(int,L.split(','))))

    pointer = 1
    for func in p:
        if func == 'R':
            pointer *= -1
        else:
            if not q:
                print('error')
                break
            else:
                q.popleft() if pointer > 0 else q.pop()

    else:
        ans = []
        while q:
            ans.append(q.popleft() if pointer > 0 else q.pop())
        print(f"[{','.join(map(str, ans))}]")