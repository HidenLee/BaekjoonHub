def solution(participant, completion):
    dic = {}
    for idx, elm in enumerate(completion):
        if elm in dic:
            dic[elm] += 1
        else:
            dic[elm] = 1
    for name in participant:
        if name not in dic or dic[name] == 0:
            return name
        dic[name] -= 1
