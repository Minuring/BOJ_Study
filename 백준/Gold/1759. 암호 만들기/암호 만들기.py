L, C = map(int, input().split())
chars = list(input().split())

moeum = [x for x in chars if x in ['a', 'e', 'i', 'o', 'u']]
jaeum = [x for x in chars if x not in moeum]

ans = []
def solve(i, pw):
    global L
    if i == C:
        if \
                len(pw) == L and \
                len([x for x in pw if x in moeum]) >= 1 and\
                len([x for x in pw if x in jaeum]) >= 2:

            ans.append(sorted(pw))
        return

    solve(i+1, pw + chars[i])
    solve(i+1, pw)

solve(0, '')
ans.sort()
for s in ans:
    print(''.join(s))