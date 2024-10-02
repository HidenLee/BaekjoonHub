for _ in range(int(input())):
    H, W, T = map(int,input().split())
    a,b = divmod(T-1,H)
    print(str(b+1)+"{:0>2}".format(str(1+a)))