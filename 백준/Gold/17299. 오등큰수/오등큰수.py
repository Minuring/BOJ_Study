#Ai가 수열 A에서 등장한횟수 = F(Ai)
#Ai의 오등큰수 Aj= 오른쪽에있으면서 Ai보다 더 자주 등장한 수 중 제일왼쪽
import sys;input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int,input().split()))
count = Counter(A)

ans = [-1] * (N+1)
stack = [0]
for i in range(1, N) :
    while stack and count[A[stack[-1]]] < count[A[i]] :
        ans[stack.pop()] = A[i]
        # print(f'i = {i}, ans : ',ans[:-1])
        # print('stack : ',stack,'\n')
    stack.append(i)

for i in range(N) :
    print(ans[i],end=' ')