import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))


def compute(op1, op2, opNumber):
    if opNumber == 0:
        return op1 + op2
    elif opNumber == 1:
        return op1 - op2
    elif opNumber == 2:
        return op1 * op2
    else:
        if op1 < 0:
            op1 *= -1
            return -1 * (op1 // op2)
        return op1 // op2


minResult, maxResult = float('inf'), -float('inf')
def calc(depth, current):
    global minResult, maxResult

    if depth == N:
        if current > maxResult:
            maxResult = current
        if current < minResult:
            minResult = current
        return

    currentNumber = nums[depth]

    for i in range(4):
        if operators[i] > 0:
            computed = compute(current, currentNumber, i)

            operators[i] -= 1
            calc(depth + 1, computed)
            operators[i] += 1


calc(1, nums[0])
print(maxResult)
print(minResult)
