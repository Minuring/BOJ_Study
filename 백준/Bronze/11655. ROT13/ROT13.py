S = input()
ans = []
for each in S :
    if each.isalpha():
        base = ord('a') if each.islower() else ord('A')
        each = chr(base+(ord(each)+13-base)%26)
    print(each, end='')