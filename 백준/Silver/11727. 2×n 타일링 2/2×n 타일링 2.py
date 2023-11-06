N = int(input())
s = [0]*1001
s[1], s[2] = 1, 3
for i in range(3, N+1) :
    s[i] = s[i-2]*2 + s[i-1]
    # print(f'{i}: {s[i-2]}*2 + {s[i-1]} = {s[i]}')

print(s[N]%10007)
