N = input().strip()
digitSum = sum(int(x) for x in N)
if '0' not in N:
    print(-1)
elif digitSum % 3 != 0:
    print(-1)
else:
    N = sorted(N, reverse=True)
    print(''.join(N))
