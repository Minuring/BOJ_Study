S = int(input())

n = 0
while S > 0:
    if S - n >= 0:
        S -= n
        n += 1
    else:
        break
print(n-1)