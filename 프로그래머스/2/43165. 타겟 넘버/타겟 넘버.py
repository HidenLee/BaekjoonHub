def solution(numbers, target):
    return sum([1 if sum([numbers[i] if mask & (1 << i) else -numbers[i] for i in range(len(numbers))]) == target else 0 for mask in range(1 << len(numbers))])
        
        
