# 백준 2447번 : 별 찍기 - 10

def printStar(n) :
    if n == 1 :
        return "*"
    
    stars = printStar(n//3)
    L = []

    for star in stars :
        L.append(star*3)
    for star in stars :
        L.append(star + ' '*(n//3) + star)
    for star in stars :
        L.append(star*3)

    return L

print( "\n".join(printStar(int(input()))) )
