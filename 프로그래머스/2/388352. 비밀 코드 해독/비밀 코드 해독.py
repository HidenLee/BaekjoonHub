def solution(n, q, ans):
    from itertools import combinations
    answer = 0
    
    for password in combinations(range(1,n+1),5):
        for i in range(len(q)):
            if len(set(list(password)+q[i])) != 10-ans[i]:
                break
        else:
            answer += 1
            
        
    return answer