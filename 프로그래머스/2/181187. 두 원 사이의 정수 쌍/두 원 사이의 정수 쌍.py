def solution(r1, r2):
    from math import ceil, floor, sqrt 
    answer = 0
    for x in range(1,r2+1):
        answer += (floor(sqrt(r2**2 - x**2)) + 1)
        answer -= (ceil(sqrt(r1**2 - x**2)) if r1 >= x else 0) 
    return answer*4

# x*2+y*2 = N*2