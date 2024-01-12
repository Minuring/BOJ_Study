import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

from itertools import combinations
teamCases = combinations(range(N), N//2)
diff = float('inf')
for team in teamCases:
    startPairs = combinations(team, 2)

    linkTeam = [x for x in range(N) if x not in team]
    linkPairs = combinations(linkTeam, 2)

    startStat, linkStat = 0, 0
    for a, b in startPairs:
        startStat += S[a][b] + S[b][a]

    for a,b in linkPairs:
        linkStat += S[a][b] + S[b][a]

    diff = min(diff, abs(startStat - linkStat))
print(diff)