
x = int(input())
a, b = divmod(x,5)
if b % 2:
    a = a - 1
    b = (b // 2) + 3
    if a < 0:
        print(-1)
    else:
        print(a+b)
else:
    print(a+b//2)