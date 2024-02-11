'''

A = 석순
B = 종유석

파괴하는 장애물 개수 = 높이 h에서 count(A[i>=h]) + count(B[H-i<=h])
count를 그냥 구하면 20만 * 50만 = 시간초과
A,B sort해서 bisect로 구하면 한 번당 2logN * 50만 = 100만 log N <= 대략 1800만 = 1초 가능

'''

import sys
input = sys.stdin.readline

N, H = map(int, input().split())
A, B = [], []
for i in range(N):
    h = int(input())
    if i % 2 == 0:
        A.append(h)
    else:
        B.append(h)

A.sort(); B.sort()
ans, ansCount = 1, N
from bisect import bisect_left
for h in range(1, H+1):
    #countA = A에서 h보다 낮은 석순의 개수 = 높이 h에서 부딪히지 않는 석순의 개수
    countA = len(A) - bisect_left(A, h)
    countB = len(B) - bisect_left(B, H-h+1)

    count_h = countA + countB
    if count_h < ansCount:
        ansCount = count_h
        ans = 1
    elif count_h == ansCount:
        ans += 1
    #O( H * logN )
    # = 50만 * 18 = 천만
print(ansCount, ans)