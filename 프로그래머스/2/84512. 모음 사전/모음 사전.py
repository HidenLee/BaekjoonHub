# 순열 완전탐색 풀이
# def solution(word): 
#     from itertools import permutations
#     return {x:y for y,x in enumerate(sorted(list(set([''.join(x) for i in range(1,6) for x in permutations(["A","E","I","O","U"]*5,i) ]))))}[word] + 1

# 5진법 풀이
# XXXXA -> XXXXE : + 1
# XXXAX -> XXXEX : + 1 + 5
# XXAXX -> XXEXX : + 1 + 5 + 25
# XAXXX -> XEXXX : + 1 + 5 + 25 + 125
# AXXXX -> EXXXX : + 1 + 5 + 25 + 125 + 625
def solution(word):
    ref1 = {"A":0, "E":1, "I":2, "O":3, "U":4}
    ref2 = [sum(5**i for i in range(j)) for j in range(5,0,-1)]
    return sum([ref1[elm]*ref2[idx]+1 for idx, elm in enumerate(word)])