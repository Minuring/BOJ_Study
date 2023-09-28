# 백준 9012번 : 괄호
def isVPS(str) :
    determine = 0
    for char in str :
        determine += 1 if ( char == '(' ) else -1
        if determine < 0 :
            return "NO"
    
    return "YES" if determine == 0 else "NO"

n = int(input())
for i in range (0, n) :
    str = input()
    print( isVPS(str) )