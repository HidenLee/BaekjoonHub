from math import gcd
X = 1000000007
def func():
    N, S = map(int, input().split())
    GCD = gcd(N,S)
    N, S = N//GCD, S//GCD
    return pow(S*pow(N,X-2,X),1,X)
print(sum([func() for _ in range(int(input()))])%X)