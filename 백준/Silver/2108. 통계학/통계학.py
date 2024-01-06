import sys;input=sys.stdin.readline
N = int(input())

numbers = [0]*N
counts = [0] * 8001

sum = 0
for i in range(N):
    num = int(input())

    counts[4000+num] += 1
    numbers[i] = num

    sum += numbers[i]

numbers.sort()
print(round(sum/N))
print(numbers[N//2])

modeCount = max(counts)
modeCandidates = sorted([num for num,x in enumerate(counts) if x == modeCount])
mode = modeCandidates[0] if len(modeCandidates) == 1 else modeCandidates[1]

print(mode - 4000)
print(numbers[N-1] - numbers[0])
