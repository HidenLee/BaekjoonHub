def solution(targets):
    targets.sort(key=lambda x:x[1])
    answer = 0
    now = -1
    for s,e in targets:
        if s<now<e:
            continue
        answer += 1
        now = e - 0.1
    return answer