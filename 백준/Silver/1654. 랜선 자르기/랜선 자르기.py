n, k = map(int, input().split())

have = []
for i in range(n):
    have.append(int(input()))

ans = 0
def solve(low, high):
    global ans, k

    if low > high: return
    mid = (low + high) // 2

    cnt = 0
    for e in have:
        cnt += e // mid

    if k <= cnt:
        ans = mid
        solve(mid + 1, high)
    else:
        solve(low, mid - 1)


solve(0, max(have) * 2)
print(ans)
