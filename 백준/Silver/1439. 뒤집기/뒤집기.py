S = input().strip()

zeroUnits = [x for x in S.split('1') if x]
oneUnits = [x for x in S.split('0') if x]

print(min(len(zeroUnits), len(oneUnits)))