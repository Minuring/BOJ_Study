import sys
input = sys.stdin.readline

S = input().rstrip()
freq = [[0 for _ in range(len(S))] for _ in range(26)]
for seq, ch in enumerate(S): #O(N)
    row = (ord(ch) - 97)
    freq[row][seq] = 1

from itertools import accumulate
for row in range(26):
    freq[row] = [0] + list(accumulate(freq[row]))

Q = int(input())
for _ in range(Q):
    tmp = input().split()
    a, l, r = tmp[0], int(tmp[1]), int(tmp[2])

    alpha = ord(a) - 97
    print(freq[alpha][r+1] - freq[alpha][l])