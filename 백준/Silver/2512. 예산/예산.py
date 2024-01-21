import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
M = int(input())

low, high = 1, max(L)
while low <= high:
    amount = (low + high) // 2
    sum_ = sum([x if x <= amount else amount for x in L])
    # print(f'{amount}원으로 상한을 정했을 때 총합 = {sum_}')

    if sum_ <= M:
        low = amount + 1
    else:
        high = amount - 1

print(high)