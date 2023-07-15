# https://www.acmicpc.net/problem/12340
# Fair and Square (Large1) 

import itertools

def generate_featable_palindrome(L):
    #generate all featable square roots of length 2*L+1 or 2*L
    yield 1
    yield 2
    yield 3

    #The case that start/end with 1 : 2n=> 1111001111,200002 / 2n+1 => 110020011,11110101111, 2001002
    #The case that start/end with 2 : 2n=> 200002 / 2n+1 => 2001002  
    for h in range(L):
        for n_ones in range(1,5):
            for ones in itertools.combinations(range(h),n_ones-1):
                a = ['0']*h
                for i in ones:
                    a[i] = '1'
                s = '1' + ''.join(a)
                rs = s[::-1]
                yield int(s+rs)
                yield int(s+'0'+rs)
                yield int(s+'1'+rs)

                if n_ones <= 2:
                    yield int(s+'2'+rs)

        s = '2' + '0'*h
        rs = s[::-1]
        yield int(s+rs)
        yield int(s+'0'+rs)
        yield int(s+'1'+rs)

all_superpalindromes = list(map(lambda x:x*x,generate_featable_palindrome(25)))

T = int(input())
for test_case in range(1,T+1):
    L, R = map(int,input().split())
    ans = 0
    for iterator in all_superpalindromes:
        if L <= iterator <= R:
            ans+=1
    print(f'Case #{test_case}: {ans}')
    
