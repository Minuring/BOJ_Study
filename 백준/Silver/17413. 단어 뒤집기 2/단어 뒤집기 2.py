import sys

input = sys.stdin.readline().rstrip()
stack = []
queue = []
i = 0
while i < len(input) :
    if input[i] == '<' :
        while stack :
            queue.append(stack.pop())

        while input[i] != '>' :
            queue.append(input[i])
            i += 1
        queue.append(input[i])

    elif input[i] == ' ' :
        while stack :
            queue.append(stack.pop())
        queue.append(input[i])

    else :
        stack.append(input[i])
    i += 1

while stack :
            queue.append(stack.pop())

print(''.join(queue))