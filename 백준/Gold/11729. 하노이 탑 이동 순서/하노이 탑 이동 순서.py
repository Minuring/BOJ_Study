process = []
def hanoii(n, start, tmp, end):
    global process
    if n == 1:
        process.append(f'{start} {end}\n')
        return

    hanoii(n-1, start, end, tmp)

    process.append(f'{start} {end}\n')

    hanoii(n-1, tmp, start, end)

N = int(input())
hanoii(N, 1, 2, 3)
print(len(process))
print(''.join(map(str, process)))