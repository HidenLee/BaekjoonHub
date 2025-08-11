def solution(weights):
    answer = 0
    dic = {x:0 for x in range(100,1001)}
    for weight in weights:
        if weight in dic:
            dic[weight] += 1

    for value in range(100,1001):
        if not dic[value]:
            continue
        answer += dic[value]*(dic[value]-1)//2
        if value * 2 <= 1000:    
            answer += dic[value*2]*dic[value]
        if (value * 3) // 2 <= 1000 and not value % 2:
            answer += dic[(value*3)//2]*dic[value]
        if (value * 4) // 3 <= 1000 and not value % 3:
            answer += dic[(value*4)//3]*dic[value]
    

    return answer