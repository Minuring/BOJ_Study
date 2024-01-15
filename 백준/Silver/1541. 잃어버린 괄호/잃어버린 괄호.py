
exp = input().strip()

minusSplit = exp.split('-')
L = [sum(map(int, x.split('+'))) for x in minusSplit]

tmp = L[0]
for i in L[1:]:
   tmp -= i

print(tmp)