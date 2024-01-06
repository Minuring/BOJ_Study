
A = int(input())
B = int(input())
C = int(input())

M = str(A*B*C)

for i in range(10):
    print(M.count(str(i)))