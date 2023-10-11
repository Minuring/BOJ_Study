import sys

input = sys.stdin.readline().strip()
stack = []
count = 0

for i in range(0, len(input)):
    
    if input[i] == ')' :
        stack.pop()

        if input[i-1] == '(' :
            count += len(stack)

        else :
            count += 1

    else :
        stack.append(input[i])
        
print(count)