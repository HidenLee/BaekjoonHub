# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3#
def solution(N, number):
    
    def setcalc(set1,set2):
        response = set([])
        for i in set1:
            for j in set2:
                response.add(i+j)
                response.add(i-j)
                response.add(j-i)
                response.add(i*j)
                if j:
                    response.add(i/j)
                if i:
                    response.add(j/i)
        return response
    
    ref = [1,11,111,1111,11111]
    finallst = []
    for i in range(9):
        temp = set([])
        if 0 < i < len(ref):
            temp.add(ref[i-1] * N)
        for j in range(1,i):
            temp.update(setcalc(finallst[j],finallst[i-j]))     
        if number in temp:
            return i
        finallst.append(temp)
        # if i == 3:
        #     print(finallst)
    return -1