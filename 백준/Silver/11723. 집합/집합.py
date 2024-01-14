import sys
input=sys.stdin.readline

M = int(input())
S = 0b0
for _ in range(M):
    str = input().split()
    command = str[0]

    if len(str) == 2:
        x = int(str[1])

        if command == 'add':
            S = S | (1 << (x-1))
        elif command == 'remove':
            S = S & ~(1 << (x-1))
        elif command == 'check':
            flag = (S & (1 << (x-1)) != 0)
            print(1 if flag else 0)
        elif command == 'toggle':
            S = S ^ (1 << (x-1))

    else :
        if command == 'all':
            S = 0b1111_1111_1111_1111_1111
        else :
            S = 0b0