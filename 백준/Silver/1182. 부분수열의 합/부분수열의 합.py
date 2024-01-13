N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
def solve(i, curSum):
    global count
    if i == N:
        if curSum == S:
            count += 1
        return

    solve(i+1, curSum + nums[i])
    solve(i+1, curSum)

solve(0, 0)
print(count if S != 0 else count-1)