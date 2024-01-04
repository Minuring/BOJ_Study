N = int(input())

numbers = [1,5,10,50]
for i in range(1,N):
    A = []
    for j in range(len(numbers)):
        for k in range(4):
            if numbers[j]+numbers[k] not in A:
                A.append(numbers[j]+numbers[k])
    numbers = A

print(len(numbers))