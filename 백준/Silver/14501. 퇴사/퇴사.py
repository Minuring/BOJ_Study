import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
tasks = []
for _ in range(N):
    tasks.append(tuple(map(int, input().split())))

ans = 0
def consulting(day, curProfit):
    global ans
    #base condition
    if day > N+1:
        return 0
    if day == N+1:
        return curProfit

    maxP = 0
    dayCost, profit = tasks[day-1]

    if dayCost == 1:
        maxP = consulting(day + 1, curProfit + profit)
    else :
        case1 = consulting(day + dayCost, curProfit + profit)
        case2 = consulting(day + 1, curProfit)
        maxP = max(case1, case2)

    return maxP

print(consulting(1, 0))
