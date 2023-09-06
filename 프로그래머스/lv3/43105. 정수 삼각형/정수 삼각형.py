def solution(triangle):
    for level in range(1,len(triangle)):
        for index in range(len(triangle[level])):
            if index == 0:
                triangle[level][index] += triangle[level-1][index]
            elif index == len(triangle[level])-1:
                triangle[level][index] += triangle[level-1][index-1]    
            else:
                triangle[level][index] += max(triangle[level-1][index-1],triangle[level-1][index]) 
    answer = max(triangle[-1])
    return answer