def solution(order):
    answer = 0
    stack = []
    for elm in range(1,len(order)+1):
        if elm == order[answer]:
            answer += 1
            continue
        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1
            continue
        stack.append(elm)
    while stack and stack[-1] == order[answer]:
        stack.pop()
        answer += 1
    return answer