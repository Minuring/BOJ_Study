N = int(input())
numbers = list(map(int,input().split()))

def isPrime(n):
    if n < 2 : return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


count = 0
for i in numbers:
    if isPrime(i):
        count += 1

print(count)
