N = int(input())
s = [0]*1001
s[1], s[2] = 1, 2
for i in range(3, N+1) :
    s[i] = s[i-2] + s[i-1]

print(s[N]%10007)