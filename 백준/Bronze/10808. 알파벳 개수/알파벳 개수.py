inputstr = list(input())

result = [0 for _ in range(ord('a'),ord('z')+1)]
for i in range(len(inputstr)):
    index = ord(inputstr[i])-ord('a')
    result[index] += 1

print(' '.join(list(map(str,result))))