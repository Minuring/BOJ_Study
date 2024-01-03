tall = [0 for i in range(9)]
for i in range(9):
    tall[i] = int(input())

def solve(n, curSum, selected):
    global tall
    if n==9 :
        if curSum == 100 and len(selected) == 7:
            selected.sort()
            for i in range(7): print(selected[i])
            quit()
        return

    selected.append(tall[n])
    solve(n + 1, curSum + tall[n], selected)

    selected.pop()
    solve(n + 1, curSum, selected)


solve(0, 0, [])
