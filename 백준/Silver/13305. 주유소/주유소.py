N = int(input())
dist = list(map(int, input().split()))
fuels = list(map(int, input().split()))

minPrice = float('inf')
cost = 0
for i, d in enumerate(dist):
    if fuels[i] < minPrice:
        cost += fuels[i] * d
        minPrice = fuels[i]
    else:
        cost += minPrice * d

print(cost)