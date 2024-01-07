
L = int(input())
S = input().rstrip()
_sum, mod = 0, 1234567891
for i, ch in enumerate(S):
    _sum += (31 ** i * ( ord(ch) - ord('a') + 1)) % mod
print(_sum % mod)