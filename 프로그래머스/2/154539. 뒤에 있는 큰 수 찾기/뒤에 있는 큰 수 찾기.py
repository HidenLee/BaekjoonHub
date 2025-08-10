from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    dq = deque([])
    maxV = 0
    for idx in range(len(numbers)-1,-1,-1):
        if maxV <= numbers[idx]:
            maxV = numbers[idx]
            dq.appendleft(numbers[idx])
            continue
        for jdx in range(idx+1,len(numbers)):
            if numbers[idx] < numbers[jdx]:
                answer[idx] = numbers[jdx]
                break
            if answer[jdx] > numbers[idx]:
                answer[idx] = answer[jdx]
                break
    return answer
        