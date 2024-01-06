T = int(input())

for _ in range(T):
    s = input().strip()

    score = 0
    prevChar, contiguous = '',1
    for ch in s:
        if ch == 'O':

            contiguous = contiguous+1 if ch==prevChar else 1

            score += contiguous

        prevChar = ch

    print(score)