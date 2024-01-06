
a,b,v = map(int,input().split())

dif = a - b
if v <= dif :
    days = 1
else :
    if (v - a) % dif == 0:
        days = (v - a) // dif + 1
    else :
        days = (v - a) // dif + 2

print(days)