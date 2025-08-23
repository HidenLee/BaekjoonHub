def solution(k, tangerine):
    dic = {}
    for tang in tangerine:
        if tang in dic:
            dic[tang] += 1
        else:
            dic[tang] = 1
    
    stack = [(x,dic[x]) for x in dic.keys()]
    stack.sort(key=lambda X:X[1])
    answer = 0
    while stack and k > 0:
        k -= stack.pop()[1]
        answer += 1
    return answer