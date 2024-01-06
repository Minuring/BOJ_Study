
s = 0
n = list(map(int, input().split()))
n = [x**2 for x in n]
print(sum(n)%10)