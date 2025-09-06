def solution(n, left, right):
    return [max(q,d)+1 for q,d in [divmod(i,n) for i in range(left,right+1)]]
