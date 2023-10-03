import sys

stack = []
answer = []
lastPushedNumber = 0

def push() :
    global lastPushedNumber
    lastPushedNumber += 1
    stack.append(lastPushedNumber)
    answer.append("+")

def myPop() :
    stack.pop()
    answer.append("-")

N = int(sys.stdin.readline())
flag = True

for _ in range (0, N) :
    input = int(sys.stdin.readline())

    while lastPushedNumber < input :
        push()

    if stack[-1] > input :
        flag = False
        break

    myPop()

if flag == True :
    print('\n'.join(answer))
else :
    print("NO")