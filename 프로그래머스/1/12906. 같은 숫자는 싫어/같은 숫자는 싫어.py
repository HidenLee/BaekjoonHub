def solution(arr):
    answer = []
    temp = -1
    for value in arr:
        if temp == value:
            continue
        answer.append(value)
        temp = value
    return answer