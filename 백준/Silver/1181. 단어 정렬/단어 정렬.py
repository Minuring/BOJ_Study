import sys;input=sys.stdin.readline

n = int(input())

strings = []
for i in range(n):
    strings.append(input().strip())

strings.sort(key=lambda x : (len(x),x))
strings = list(dict.fromkeys(strings))
for i in strings:
    print(i)