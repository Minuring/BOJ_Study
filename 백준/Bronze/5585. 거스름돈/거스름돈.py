price = 1000 - int(input())
coins = [1,5,10,50,100,500]

count = 0
while price > 0:
    coin = coins.pop()
    amount = price // coin
    count += amount
    price = price % coin
print(count)