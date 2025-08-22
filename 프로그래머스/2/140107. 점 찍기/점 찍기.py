import math
def solution(k, d):
    answer = 0
    i = 0
    while i*k <= d:
        answer += (math.sqrt(d**2-(i*k)**2)//k + 1) 
        # print(answer)
        
        i+=1
    return answer