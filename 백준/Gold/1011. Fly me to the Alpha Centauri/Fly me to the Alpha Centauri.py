for test_case in range(int(input())):
    x, y = map(int,input().split())
    D = y-x
    d = int(D**(1/2))
    if d**2 == D:
        print(2*d-1)
    elif D <= d*(d+1):
        print(2*d)
    elif D < (d+1)**2:
        print(2*d+1)