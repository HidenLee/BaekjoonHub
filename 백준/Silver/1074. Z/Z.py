#https://www.acmicpc.net/problem/1074


def func(n,r,c):
    if n == 0:
        return r * 2 + c

    midx = 2**(n-1)
    # print(n,r,c,midx)
    
    # NWx1 NEx2 SWx3 SEx4
    if r < midx and c < midx:
        return func(n-1,r,c)

    elif r < midx and c >= midx: 
        return func(n-1,r,c-midx) + 1*4**(n-1)
    
    elif r >= midx and c < midx: 
        return func(n-1,r-midx,c) + 2*4**(n-1)
    
    elif r >= midx and c >= midx:
        return func(n-1,r-midx,c-midx) + 3*4**(n-1)
    else:
        #????
        return 0



N, r, c = map(int, input().split())
print(func(N,r,c))