N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
def solve(i, L, curSum):
    global count
    if i == N:
        if L and curSum == S:
            count += 1
        return

    solve(i+1, L + [nums[i]], curSum + nums[i])
    solve(i+1, L, curSum)

solve(0, [], 0)
print(count)