def solution(players, callings):
    dic1 = {idx:name for idx,name in enumerate(players)}
    dic2 = {name:idx for idx,name in enumerate(players)}
    for name1 in callings:
        idx2 = dic2[name1]
        idx1 = idx2 - 1
        name2 = dic1[idx1]
        dic1[idx1] , dic1[idx2] = dic1[idx2] , dic1[idx1]
        dic2[name1], dic2[name2] = dic2[name2], dic2[name1]
        
    return [dic1[i] for i in range(len(players))]