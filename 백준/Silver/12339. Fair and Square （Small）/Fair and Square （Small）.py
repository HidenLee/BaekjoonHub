# https://www.acmicpc.net/problem/12340
# Fair and Square (Large1) 


def ispalindrome(x):
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    else:
        return True


def issquare(x):
    return True if int(x**0.5)**2 == x else False


def issuperpalindrome(x): 
    return True if issquare(x) and ispalindrome(x) and ispalindrome(int(x**0.5)) else False



T = int(input())
for test_case in range(1,T+1):
    L, R = map(int,input().split())
    ans = 0
    for iterator in range(L,R+1):
        if issuperpalindrome(iterator):
            ans += 1
    print(f'Case #{test_case}: {ans}')
    