def solution(name):
    answer = [min(ord(x)-ord("A"),ord("Z")-ord(x)+1) for x in name]
    
    adjust = len(name) - 1
    for i in range(len(name)):
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        adjust = min(adjust, 2*i + len(name) - next_idx) #left turn right
        adjust = min(adjust, i + 2*(len(name) - next_idx)) #right turn left
    return sum(answer) + adjust 
    