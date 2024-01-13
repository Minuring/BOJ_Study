N, K = map(int, input().split())

nums = []
for i in range(1, int(N**(1/2))+1):

    if N % i == 0:
        nums.append(i)
        if i ** 2 != N:
            nums.append(N // i)

if len(nums) < K:
    print(0)
else :
    print(sorted(nums)[K-1])