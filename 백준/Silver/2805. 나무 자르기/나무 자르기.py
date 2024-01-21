import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

low, high = 1, trees[-1]
while low <= high:
    cut = (low + high) // 2
    get = sum([x - cut for x in trees if x > cut])

    if get < M:
        high = cut - 1
    else:
        low = cut + 1
    # print(f'{cut}으로 잘랐을 때 get = {get}')
print((low+high)//2)