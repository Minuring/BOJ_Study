def permutation(string, picked, seq):
    # i번째 수 선택 -> i+1이후부터 j번째 수 선택
    global found
    if len(picked) == len(string):
        found += 1
        return "".join(string[i] for i in picked) if found == seq else None

    result = None
    for i in range(len(string)):
        if i not in picked:
            picked.append(i)
            result = permutation(string, picked, seq)
            picked.remove(i)
        if result is not None:
            break

    return result


while True:
    try:
        string, seq = input().split()
        seq = int(seq)

        found = 0
        result = permutation(string, list(), seq)
        print(f'{string} {seq} = ', end='')
        if result is None:
            print('No permutation')
        else:
            print(result)
    except EOFError:
        break
