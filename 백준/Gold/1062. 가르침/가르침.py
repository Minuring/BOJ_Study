
'''
1 <= N <= 50
1 <= K <= 26
a c i n t

'''
from itertools import combinations
teachedDefault = 0b1010_0000_1000_0100_0001_0000_00
needToTeach = [x for x in range(26) if x not in [0,2,8,13,19]]
N, K = map(int, input().split())

if K < 5:
    print(0)

else:
    words = []
    for _ in range(N):
        w = input().rstrip()
        b = 0b0
        for a in set(w):
            nthBit = ord(a)-97
            b += (1 << (25 - nthBit))
        words.append(b)
    maxCount = 0
    for comb in combinations(needToTeach, K-5):
        teached = teachedDefault
        for idx in comb:
            teached = teached | (1 << (25-idx))
            # print(f'{idx}({chr(65+idx)}) -- { 1<<(25-idx) }')

        count = 0
        for word in words:
            if ~teached & word == 0:
                count += 1
        maxCount = max(maxCount, count)

    print(maxCount)