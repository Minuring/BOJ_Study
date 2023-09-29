import sys

stack = []
top = -1

n = int(input())

for i in range(0, n) :
    cmd = sys.stdin.readline().replace("\n","").split(" ")

    if cmd[0] == "push" :
        stack.append(cmd[1])
        top += 1

    elif cmd[0] == "pop" :
        if top == -1 :
            print(-1)
        else :
            top -= 1
            print( stack.pop() )

    elif cmd[0] == "size" :
        print( top + 1 )

    elif cmd[0] == "empty" :
        print( ("1" if top==-1 else "0") )

    else : 
        print( ("-1" if top == -1 else stack[top]))