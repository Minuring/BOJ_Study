import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)
usedRopes = [ropes[0]]
for w in ropes[1:]:
    usedRopes.append(w * (len(usedRopes)+1))


print(max(usedRopes))