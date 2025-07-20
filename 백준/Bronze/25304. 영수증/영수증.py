print("Yes" if (a:=int(input())) == sum(int(x)*int(y) for _ in range(int(input())) for x,y in [input().split()]) else "No")
