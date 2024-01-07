import sys;input=sys.stdin.readline

n=int(input())

inputList = []
for i in range(n):
    x, y = map(int, input().split())
    inputList.append((x,y))

for person in inputList:

    count = 0
    for other in inputList:
        if person is not other\
            and person[0] < other[0] and person[1] < other[1]:
            count += 1
    print(count + 1, end =' ')
