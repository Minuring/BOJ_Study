def cantor(N) :
    if N == 1 :
        return "-"
    line = cantor(N//3) + ' '*(N//3) + cantor(N//3)
    return line

while True :
    try :
        N = int(input())
        print(cantor(3**N))
    except :
        break

