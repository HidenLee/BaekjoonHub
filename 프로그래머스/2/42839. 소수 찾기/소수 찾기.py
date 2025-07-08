def solution(numbers):
    isPrime = [True] * 10000000
    isPrime[0] = isPrime[1] = False
    for i in range(2,int(10000000**0.5)+1):
        if isPrime[i]:
            for j in range(i*i,10000000,i):
                isPrime[j] = False
    
    from itertools import permutations
    return sum(1 if isPrime[x] else 0 for x in set(int(''.join(x)) for i in range(1,len(numbers)+1) for x in permutations(numbers,i)))
