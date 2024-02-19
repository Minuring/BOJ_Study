import sys
sys.setrecursionlimit(10**6)
def dfs(i, cards, visited):
    visited[i] = True
    return 1 + (dfs(cards[i]-1, cards, visited) if not visited[cards[i]-1] else 0)

def solution(cards):
    
    N = len(cards)
    visited = [False for _ in range(N+1)]
    answer = 0
    group = []
    for i in range(N):
        if not visited[i]:
            group.append(dfs(i, cards, visited))
    
    group.sort()
    if len(group) == 1:
        return 0
    return group[-1] * group[-2]