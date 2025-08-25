def solution(topping):
    left = set()
    right = {}
    for elm in topping:
        if elm in right:
            right[elm] += 1
        else:
            right[elm] = 1
    
    rcount = len(right.keys())
    answer = 0

    for elm in topping:
        left.add(elm)
        right[elm] -= 1
        if right[elm] == 0:
            rcount -= 1
        if len(left) == rcount:
            answer += 1

    return answer