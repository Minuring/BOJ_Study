N = int(input())
A = set(map(int, input().split()))
M = int(input())

test = list(map(int, input().split()))
for i in range(M):
    print(1 if test[i] in A else 0)