import re
import sys;input=sys.stdin.readline
while True:
    try:
        s = input().rstrip()
        if not s or s == '.':
            break

        l = re.findall(r'[\[\]().$]', s)

        stack, result = [], False
        for e in l:
            if e == '.' and e == s[-1]:
                result = False if stack else True
                break

            if e == '(' or e == '[':
                stack.append(e)

            else:
                if not stack:
                    break
                if (e == ')' and stack[-1] == '(')\
                    or (e == ']' and stack[-1] == '['):
                    stack.pop()
                else :
                    break

            # print(f'- {e} 처리 후 stack : {stack}')

        print('yes' if result else 'no')

    except EOFError:
        break