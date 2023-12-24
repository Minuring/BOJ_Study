S = list(input())
L = [S]
for i in range(1,len(S)):
    L.append(S[i:])
L.sort()
print('\n'.join([''.join(row) for row in L]))