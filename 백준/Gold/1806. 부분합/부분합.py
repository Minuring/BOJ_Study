N, S = map(int, input().split())
A = list(map(int, input().split()))

currentSum, left, right = 0, 0, 0
currentMinLength = float('inf')
while True:
    if currentSum >= S:
        currentMinLength = min(currentMinLength, right - left)
        currentSum -= A[left]
        left += 1
    else :
        if right == N:
            break
        currentSum += A[right]
        right += 1

print(currentMinLength if currentMinLength != float('inf') else 0)