def solution(sequence, k):
    left = right = len(sequence) - 1
    num = sequence[right]
    
    while num > k:
        left -= 1
        right -= 1
        num = sequence[right]
    while num < k:
        left -= 1
        num += sequence[left]
        if num > k:
            num -= sequence[right]
            right -= 1
    while left >= 1 and sequence[left-1] == sequence[right]:
        left -= 1
        right -= 1
    return [left,right]
    