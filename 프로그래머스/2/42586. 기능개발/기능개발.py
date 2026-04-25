def solution(progresses, speeds):
    import math
    answer = []
    count = 1
    temp = -1
    for days in [math.ceil((100-progresses[x]) / speeds[x]) for x in range(len(progresses))]:
        if temp >= days:
            count += 1
            continue
        if temp != -1:
            answer.append(count)
        temp = days
        count = 1
    temp = len(progresses) - sum(answer)
    if temp:
        answer.append(temp)
    
    return answer