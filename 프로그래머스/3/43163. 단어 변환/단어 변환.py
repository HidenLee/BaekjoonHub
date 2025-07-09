def solution(begin, target, words):
    def match(str1,str2):
        flag = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                continue
            if flag == 1:
                return False
            flag += 1
        return True
    dic = {x:[y for y in words if x != y and match(x,y)] for x in words}
    answer = len(words) + 1
    for start in dic.keys():
        if match(begin,start):
            visit = set(start)
            stack = [(start,1)]
            while stack:
                now, depth = stack.pop()
                if now == target:
                    answer = min(answer,depth)
                for nxt in dic[now]:
                    if not nxt in visit:
                        visit.add(nxt)
                        stack.append((nxt,depth+1))
    return 0 if answer == len(words) + 1 else answer