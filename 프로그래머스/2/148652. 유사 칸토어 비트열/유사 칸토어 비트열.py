def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        while True:
            if i < 5 and i != 2:
                answer +=1
                break
            if (i - 2) % 5 == 0:
                break
            i //= 5
                
    return answer