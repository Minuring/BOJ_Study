
A,B,C,X,Y = map(int,input().split())

cost = 0
if A + B > C * 2 :
    minXY = min(X,Y)

    cost += C * 2 * minXY
    X -= minXY
    Y -= minXY

    if X == 0:
        cost += Y * (B if B<C*2 else C*2)
    else :
        cost += X * (A if A<C*2 else C*2)

else :
    cost += A * X
    cost += B * Y

print(cost)