def d(n):
    return n + sum(map(int, str(n)))

numbers = list(range(1, 10001))

for i in range(1, 10001):
    num = d(i)
    if num in numbers:
        numbers.remove(num)

for num in numbers:
    print(num)
