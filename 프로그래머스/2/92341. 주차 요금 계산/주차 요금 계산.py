def solution(fees, records):
    import math
    dic = {}
    answer = []
    for record in records:
        time, number, flag = record.split()
        time = int(time[:2])*60 + int(time[3:])
        if not number in dic:
            dic[number] = [[time],True if flag == "IN" else False]
        else:
            dic[number][0].append(time)
            dic[number][1] = True if flag == "IN" else False
    for key in dic:
        if dic[key][1]:
            dic[key][0].append(23*60+59)
        count = sum([dic[key][0][i]-dic[key][0][i-1] for i in range(1,len(dic[key][0]),2)])
        answer.append((key,fees[1] if fees[0] >= count else fees[1] + math.ceil((count-fees[0])/fees[2])*fees[3]))
    return [x[1] for x in sorted(answer,key=lambda x:x[0])]