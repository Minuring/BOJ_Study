while True:
    try:
        n = list(input().lstrip('0'))

        if not n:
            break

        s, e = 0, len(n)-1
        n = list(n)
        flag = True
        while s < e:
            if n[s] != n[e]:
                flag = False
                break
            s += 1
            e -= 1

        print("yes" if flag else "no")
    except:
        break
