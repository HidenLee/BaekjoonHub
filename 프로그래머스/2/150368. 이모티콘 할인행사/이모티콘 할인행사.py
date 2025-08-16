def solution(users, emoticons):
    from itertools import product
    n = len(users)
    m = len(emoticons)
    ref = {0:10,1:20,2:30,3:40}
    answer = [0,0]
    for case in list(product(range(4),repeat=m)):
        total = 0
        subscribe = 0
        for rate,maxV in users:
            sumV = sum([(100-ref[case[idx]])*emoji//100 for idx, emoji in enumerate(emoticons) if rate <= ref[case[idx]]])
            if sumV >= maxV:
                subscribe += 1
            else:
                total += sumV
        
        if answer[0] < subscribe:
            answer[0] = subscribe
            answer[1] = total
        elif answer[0] == subscribe:
            answer[1] = max(answer[1],total)
            
            
    
    
    return answer