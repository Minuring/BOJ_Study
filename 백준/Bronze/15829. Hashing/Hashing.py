
L = int(input())
S = input().rstrip()
_sum = 0
for i, ch in enumerate(S):
    _sum += (31 ** i * ( ord(ch) - ord('a') + 1))
print(_sum)