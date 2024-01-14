def solution(k, m, score):
    answer = 0
    
    score.sort()
    while len(score) >= m:
        box = [score.pop() for _ in range(m)]
        answer += box[-1] * len(box)
    
    return answer
    
    
    
    
    