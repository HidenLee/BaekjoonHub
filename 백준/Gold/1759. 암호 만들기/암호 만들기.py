from itertools import combinations

N, M = map(int, input().split())
arr = list(input().split())
arr.sort()  # Simple lexicographical sort

vowels = set("AEIOUaeiou")

for comb in combinations(arr, N):
    jcnt = 0
    mcnt = 0
    
    for elm in comb:
        if elm in vowels:
            mcnt += 1
        else:
            jcnt += 1
    
    # Check if the combination is valid
    if jcnt >= 2 and mcnt >= 1:
        print("".join(comb))