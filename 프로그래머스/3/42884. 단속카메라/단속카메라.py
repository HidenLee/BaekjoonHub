def solution(routes):
    now = -30001
    answer = 0

    for fr,to in sorted(routes,key=lambda X:X[1]):
        if fr <= now:
            continue
        now = to
        answer += 1
    return answer