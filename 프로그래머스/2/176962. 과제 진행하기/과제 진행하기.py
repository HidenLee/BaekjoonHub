def solution(plans):
    p = [(x[0],int(x[1][:2])*60 + int(x[1][3:]),int(x[2])) for x in plans]
    p.sort(key= lambda x: -x[1])
    first = p.pop()
    now = first[1]
    stack = [(first[0],first[2])]
    
    answer = []

    while p:
        if now < p[-1][1]:
            diff = p[-1][1] - now
            now = p[-1][1]
            while stack:
                sub, cost = stack.pop()
                diff -= cost
                if diff < 0:
                    stack.append((sub,-diff))
                    break
                answer.append(sub)
        elif now == p[-1][1]:
            plan = p.pop()
            stack.append((plan[0],plan[2]))
    while stack:
        answer.append((stack.pop())[0])
    return answer