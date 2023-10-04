import sys

input = sys.stdin.readline().rstrip()
before_Cursor_Stack = list(input)
after_Cursor_Stack = []
M = int(sys.stdin.readline())
for i in range(M) :
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'L' :
        if before_Cursor_Stack :
            after_Cursor_Stack.append(before_Cursor_Stack.pop())
    elif cmd[0] == 'D' :
        if after_Cursor_Stack :
            before_Cursor_Stack.append(after_Cursor_Stack.pop())
    elif cmd[0] == 'B' :
        if before_Cursor_Stack:
            before_Cursor_Stack.pop()
    else :
        before_Cursor_Stack.append(cmd[1])
        
before_Cursor_Stack.extend(reversed(after_Cursor_Stack))
print("".join(before_Cursor_Stack))