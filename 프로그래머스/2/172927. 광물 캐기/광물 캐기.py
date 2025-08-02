def solution(picks, minerals):
    dic = {"diamond":25,"iron":5,"stone":1}
    minerals = minerals[:min(len(minerals),sum(picks)*5)]
    m = [dic[x] for x in minerals]
    ref = sorted([(sum([x for x in m[i*5:(i+1)*5]]),i) for i in range(((len(m)-1)//5)+1)],reverse=True)
    answer = 0
    for _,idx in ref:
        if picks[0] > 0:
            picks[0] -= 1
            pick = 25
        elif picks[1] > 0:
            picks[1] -= 1
            pick = 5
        elif picks[2] > 0:
            picks[2] -= 1
            pick = 1
        else:
            break
        answer += sum([max(x//pick,1) for x in m[idx*5:(idx+1)*5]])
    return answer