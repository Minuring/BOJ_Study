N, K = map(int, input().split())

L = [i for i in range(1,N+1)]

ptr = 0
ans = []
while L:
    ptr = (ptr + K) % len(L)

    ans.append(L.pop(ptr-1))
    ptr = (ptr - 1) if ptr > 0 else len(L)

print('<', ', '.join(map(str, ans)),'>',sep='')