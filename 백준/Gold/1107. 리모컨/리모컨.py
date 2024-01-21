import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = []
if M > 0:
    broken = list(map(int, input().split()))

minCount = abs(100 - N)
for n in range(999900):

    for digit in str(n):
        if int(digit) in broken:
            break

    else:
        count = abs(n - N) + len(str(n))
        if count < minCount:
            # print(f'{n}에서 count={count}')
            minCount = count

print(minCount)