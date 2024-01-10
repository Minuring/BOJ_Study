N = int(input())
def isHansu(n):
    if n < 100 : return True
    # assert n >= 100
    digits = list(map(int, list(str(num))))

    dif = digits[0] - digits[1]
    for i in range(1, len(digits)-1):
        if digits[i] - digits[i+1] != dif:
            return False

    return True


count = 0
for num in range(1, N+1):
    if isHansu(num):
        count += 1

print(count)