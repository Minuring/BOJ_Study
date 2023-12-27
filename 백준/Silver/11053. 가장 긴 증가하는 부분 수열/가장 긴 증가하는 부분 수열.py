N = int(input())
A = list(map(int,input().split()))
length = [1] * N

for i in range(1,N):
    candidates = [x for x in range(i) if A[x] < A[i]]
    if candidates:
        maxLen = max(candidates, key=lambda x:length[x])
        length[i] = length[maxLen]+1
    else:
        length[i] = 1

print(max(length))
