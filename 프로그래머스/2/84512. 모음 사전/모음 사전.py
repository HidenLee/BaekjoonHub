def solution(word):
    from itertools import permutations
    return {x:y for y,x in enumerate(sorted(list(set([''.join(x) for i in range(1,6) for x in permutations(["A","E","I","O","U"]*5,i) ]))))}[word] + 1