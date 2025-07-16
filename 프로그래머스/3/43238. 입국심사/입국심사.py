def solution(n, times):
    right = n * 10e9 + 1
    left = 0
    answer = 0
    while left <= right:
        mid = (left+right)//2
        count = 0
        for time in times:
            count += mid // time
            if count >= n:
                break
        if count >= n:
            answer = mid
            right = mid - 1
            continue
        left = mid + 1
    return answer