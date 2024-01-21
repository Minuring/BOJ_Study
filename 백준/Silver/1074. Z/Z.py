def getSeq(N, r, c, seq):
    maxSeq = 2**(2*N) - 1
    # print(f'N={N}, r={r}, c={c}, seq={seq}, maxSeq={maxSeq}')
    # print(f'parts={seq}, {seq+maxSeq//4}, {seq+maxSeq//2}, {seq+(maxSeq*3)//4}')
    # print()
    if r >= 2**(N-1):
        seq += maxSeq//2 + 1
    if c >= 2**(N-1):
        seq += maxSeq//4 + 1

    if N > 1:
        r = r if r < 2 ** (N - 1) else r - 2 ** (N-1)
        c = c if c < 2 ** (N - 1) else c - 2 ** (N-1)
        seq = getSeq(N-1, r, c, seq)

    return seq


N, R, C = map(int, input().split())
print(getSeq(N, R, C, 0))