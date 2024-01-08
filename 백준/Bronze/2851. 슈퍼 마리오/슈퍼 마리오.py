score = 0
for _ in range(10):
    nextScore = int(input())
    afterScore = score + nextScore

    if afterScore >= 100:
        beforeDiff = 100 - score
        afterDiff = afterScore - 100

        if afterDiff <= beforeDiff:
            score = afterScore
        break

    else:
        score += nextScore
print(score)
