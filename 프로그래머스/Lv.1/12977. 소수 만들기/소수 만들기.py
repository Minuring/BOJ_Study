from itertools import combinations
def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for comb in combinations(nums, 3):
        if isPrime(sum(comb)):
            answer += 1

    return answer