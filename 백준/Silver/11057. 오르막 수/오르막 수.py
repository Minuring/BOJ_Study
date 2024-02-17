s = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
N = int(input())

for i in range(2, N):
    for x in range(1, 10):
        s[x] = (s[x-1] + s[x]) % 10007

if N == 1:
    print(10)
else:
    print(s[-1] % 10007)
