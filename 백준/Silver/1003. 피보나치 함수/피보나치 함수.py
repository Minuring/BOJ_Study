import sys
input = sys.stdin.readline

zeros, ones = [0]*41, [0]*41
zeros[0], ones[1] = 1, 1
for i in range(2, 41):
    zeros[i] = zeros[i-1] + zeros[i-2]
    ones[i] = ones[i-1] + ones[i-2]

T = int(input())
for _ in range(T):
    N = int(input())

    print(zeros[N], ones[N])