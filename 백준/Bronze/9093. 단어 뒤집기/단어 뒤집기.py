import sys

def rev(str):
    return str[::-1]

N = int(sys.stdin.readline())

output = ""
for i in range(0, N) :
    line = list(map(rev,sys.stdin.readline().strip().split()))
    output += " ".join(line) + "\n"

print(output)