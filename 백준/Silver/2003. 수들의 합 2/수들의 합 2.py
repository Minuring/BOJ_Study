N ,M = map(int,input().split())

A = list(map(int,input().split()))

l, r, curSum = 0, 0, 0
count = 0
while True:
    if curSum == M:
        count += 1
        curSum -= A[l]
        l += 1

    elif curSum < M:
        if r == N: break
        curSum += A[r]
        r += 1

    else:
        curSum -= A[l]
        l += 1

print(count)