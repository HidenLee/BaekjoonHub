def solution(answers):
    ref1 = [1,2,3,4,5]
    ref2 = [2,1,2,3,2,4,2,5]
    ref3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for idx,value in enumerate(answers):
        if ref1[idx%5] == value:
            count[0] += 1
        if ref2[idx%8] == value:
            count[1] += 1
        if ref3[idx%10] == value :
            count[2] += 1
    temp = 0
    answer = []
    for i in [0,1,2]:
        if temp < count[i]:
            temp = count[i]
            answer = [i+1]
        elif temp == count[i]:
            answer.append(i+1)
        
    return answer