def solution(n, lost, reserve):
    dic = {x:True for x in reserve}
    lost_remain = []
    for l in lost:
        if l in dic and dic[l]:
            dic[l] = False
            continue
        lost_remain.append(l)
    lost_remain.sort()
    for l in lost_remain:
        if l - 1 in dic and dic[l-1]:
            dic[l-1] = False
            continue
        if l + 1 in dic and dic[l+1]:
            dic[l+1] = False
            continue
        n -= 1
    return n