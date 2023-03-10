T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = (x1-x2)**2 + (y1-y2)**2
    if (x1,y1,r1) == (x2,y2,r2):
        print(-1)
    else:
        if distance in [(r1+r2)**2,(r1-r2)**2]:
            print(1)
        elif distance > (r1+r2)**2:
            print(0)
        else:
            if distance < (r1-r2)**2:
                print(0)
            else:
                print(2)