
asc = [i for i in range(1,9)]
desc = [i for i in range(8,0,-1)]

l = list(map(int, input().split()))

if l == asc :
    print("ascending")
elif l == desc:
    print("descending")
else : print("mixed")
