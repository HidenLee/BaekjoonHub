def solution(clothes):
    dic = {}
    for elm, typ in clothes:
        if typ in dic:
            dic[typ].append(elm)
        else:
            dic[typ] = [elm]
    answer = 1
    for key in dic.keys():
        answer *= (len(dic[key]) + 1)
    return answer - 1