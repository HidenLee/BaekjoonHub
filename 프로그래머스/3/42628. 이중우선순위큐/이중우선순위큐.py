def solution(operations):
    import heapq
    maxQ = []
    minQ = []
    isValid = []
    answer = []
    for op in operations+["P  ","P -"]:
        
        if op[0] == "I":
            isValid.append(True)
            heapq.heappush(maxQ,(-int(op[2:]),len(isValid)-1))
            heapq.heappush(minQ,(int(op[2:]),len(isValid)-1))
            continue
        target = minQ if op[2] == "-" else maxQ 
        while target:
            value, idx = heapq.heappop(target)
            if isValid[idx]:
                if op[0] == "P":
                    answer.append(value)
                    break
                isValid[idx] = False
                break

    return [-answer[0],answer[1]] if answer  else [0,0]