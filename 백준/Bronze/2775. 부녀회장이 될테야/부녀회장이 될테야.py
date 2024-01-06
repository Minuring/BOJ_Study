T = int(input())

table = [[1 for _ in range(14)] for _ in range(15)]
table[0] = [i for i in range(1,15)]

for floor in range(1,15):
    for ho in range(1,14):
        table[floor][ho] = table[floor][ho-1] + table[floor-1][ho]

for _ in range(T):
    k = int(input())
    n = int(input())

    print(table[k][n-1])
