
form = list(input())
prev = ''
result = 1
for ch in form:
    if prev == ch :
        if ch == 'd':
            result *= 9
        elif ch == 'c':
            result *= 25
    else :
        if ch == 'd':
            result *= 10
        elif ch == 'c':
            result *= 26
    prev = ch

print(result)