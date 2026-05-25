def solution1(info, query):
    dic = {"cpp":[],"java":[],"python":[],"backend":[],"frontend":[],"junior":[],"senior":[],"chicken":[],"pizza":[],"-":[x for x in range(len(info))]}
    rank = [0 for _ in range(len(info))]
    for idx, detail in enumerate(info):
        d = detail.split()
        for jdx in range(4):
            dic[d[jdx]].append(idx)
        rank[idx] = int(d[-1])
    def solve(ipt):
        def intersectionArrays(arr):
            def intersection(arr1,arr2):
                new_array = []
                flag = {}
                for elm in arr1:
                    flag[elm] = True
                for elm in arr2:
                    if elm in flag:
                        new_array.append(elm)
                return new_array
            
            new_array = arr[0]
            for nxt in arr[1:]:
                new_array = intersection(new_array,nxt)
            return new_array
        
        answer = 0        
        commands = list(ipt.split())
        for candidate in intersectionArrays([dic[commands[0]], dic[commands[2]], dic[commands[4]], dic[commands[6]]]):
            answer += 1 if rank[candidate] >= int(commands[-1]) else 0 
            
        return answer
    return [solve(q) for q in query]


import bisect
def solution(info,query):
    lang = ["cpp","java","python"]
    job = ["backend","frontend"]
    age = ["junior","senior"]
    soul = ["chicken","pizza"]
    cursor = {0:lang,1:job,2:age,3:soul}
    dic = {v: {x: {y: {z:[] for z in soul} for y in age} for x in job} for v in lang}
    for detail in info:
        d = detail.replace("and ","").split()
        d[-1] = int(d[-1])
        idx = bisect.bisect_left(dic[d[0]][d[1]][d[2]][d[3]],d[-1])
        dic[d[0]][d[1]][d[2]][d[3]].insert(idx,d[-1])
    
    def solve(query):
        if not isinstance(query,list):
            query = query.replace("and ","").split()
        target = int(query[-1])
        now = dic
        for idx, keyw in enumerate(query[:4]):
            if keyw == "-":
                return sum([solve(query[:idx] + [x] + query[idx+1:]) for x in cursor[idx]])
            now = now[keyw]
        else:
            return len(now) - bisect.bisect_left(now,target)
        
        
        
    return [solve(q) for q in query]      
