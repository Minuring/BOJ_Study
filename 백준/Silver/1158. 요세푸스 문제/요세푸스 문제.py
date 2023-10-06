import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
q = deque()
answer = []

for i in range(1, N+1) :
    q.append(i)

while q :
    for _ in range(0, K-1) :
        q.append(q.popleft())
    
    answer.append(q.popleft())

print('<' + ', '.join(map(str,answer)) + '>')
