chess = [[(i+p)%2 for i in range(8)] for p in range(8)]
for a,b in [tuple(input().split()) for _ in range(int(input()))]:
    print("YES" if chess[int(a[1])-1][ord(a[0])-ord("A")]==chess[(int(b)-1)//8][(int(b)-1)%8] else "NO")