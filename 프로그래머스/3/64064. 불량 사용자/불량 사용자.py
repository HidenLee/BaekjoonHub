from itertools import product
def solution(user_id, banned_id):
    answer = []
    def compare(str1,str2):
        if len(str1) == len(str2):
            for idx in range(len(str1)):
                if str2[idx] != '*' and str1[idx] != str2[idx]:
                    return False                        
            else:
                return True
        return False
    lst = [[] for _ in range(len(banned_id))]        
    for banidx in range(len(banned_id)):
        for useridx in range(len(user_id)):
            if compare(user_id[useridx],banned_id[banidx]):
                lst[banidx].append(useridx)
    answer = list(tuple(sorted(subset)) for subset in product(*lst) if len(set(subset))==len(banned_id))
    final = []
    # for idx in range(len(answer)):
    #     answer[idx] = list(set(answer[idx]))
    #     if len(answer[idx]) == len(banned_id):
            # final.append(answer[idx])
    # print(answer)
    # final = list(set([tuple(set(subset)) for subset in final])) 
    return len(set(answer))