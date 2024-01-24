import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

LCS = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])