def solution(n):
    answer = [0 for _ in range(2001)]
    answer[1] = 1
    answer[2] = 2
    for i in range(3,n+1):
        answer[i] = answer[i-2] + answer[i-1]
    return answer[n] % 1234567