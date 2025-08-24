def solution(k, ranges):
    answer = []
    x = 0
    dic = {0:k}
    
    while k != 1:
        if k % 2:
            k = k*3 + 1
        else:
            k //= 2
        x += 1
        dic[x] = k
        
    for st,ed in ranges:
        ed = x + ed
        if st > ed:
            answer.append(-1)
        else:
            answer.append(sum([ (y1+y2)/2 for y1,y2 in [(dic[i],dic[i+1])for i in range(st,ed)]]))
    return answer