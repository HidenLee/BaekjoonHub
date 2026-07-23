def solution(e, starts):
    count = [0 for _ in range(e+1)]
    for i in range(1,e+1):
        for ii in range(i,e+1,i):
            count[ii] += 1
            
    answer = [0 for _ in range(e+1)]
    answer[e] = e
    
    for i in range(e-1,0,-1):
        if count[i] >= count[answer[i+1]]:
            answer[i] = i
        else:
            answer[i] = answer[i+1]
            
    return [answer[s] for s in starts]