def solution(sizes):
    sizes = [sorted(x) for x in sizes]
    
    return max([x[0] for x in sizes]) * max(x[1] for x in sizes)