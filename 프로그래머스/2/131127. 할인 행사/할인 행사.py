from collections import Counter
def solution(want, number, discount):
    discount = ["blank"] + discount
    answer = 0
    left = 0
    count = Counter(discount[:10])
    for new in discount[10:]:
        count[discount[left]] -= 1
        count[new] += 1        
        answer += 1 if all([True if number[idx] == count[x] else False for idx, x in enumerate(want)]) else 0
        left += 1
        
    return answer