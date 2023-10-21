
from collections import deque
N = int(input())
calc = deque(list(input()))

numbers = []
for i in range(N):
    numbers.append(input())


operand = []
for _ in range(len(calc)) :
    element = calc.popleft()
    if element == '+' or element == '-' or element == '*' or element == '/' :
        opnd2, opnd1 = operand.pop(), operand.pop()
        compute = str(opnd1) + element + str(opnd2)

        operand.append(eval(compute))
    else :
        operand.append(numbers[ord(element)-ord('A')])

print('%.2f' %operand[0])