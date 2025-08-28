def solution(elements):
    N = len(elements)
    answer = set()
    elements *= 2
    for i in range(len(elements)):
        for j in range(i,len(elements)):
            if j - i < N:
                answer.add(sum(elements[i:j]))
    return len(answer)