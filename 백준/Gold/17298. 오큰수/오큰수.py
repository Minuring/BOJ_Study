import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
answer = [-1] * N
stack = []

for i in range(N) :

    while stack and array[stack[-1]] < array[i] :
        # stack[-1] : 이전 순서, array[stack[-1]] : 이전 숫자
        answer[stack.pop()] = array[i]

    stack.append(i) #조건에 관계없이 stack에 push index

print(*answer)