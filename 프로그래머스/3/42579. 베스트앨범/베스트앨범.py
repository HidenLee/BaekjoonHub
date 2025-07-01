def solution(genres, plays):
    answer = []
    dic = {X:[0,[(-1,-1),(-1,-1)]] for X in set(genres)}
    
    for idx, value in enumerate(plays):
        typ = genres[idx]
        dic[typ][0] += value
        dic[typ][1] = sorted(dic[typ][1] + [(value,idx)],key=lambda X:(X[0],-X[1]))[1:][::-1]
    for _, songs in sorted(dic.values(),key=lambda X:-X[0]):
        if songs[0][1] != -1:
            answer.append(songs[0][1])
        if songs[1][1] != -1:
            answer.append(songs[1][1])       
    
    return answer