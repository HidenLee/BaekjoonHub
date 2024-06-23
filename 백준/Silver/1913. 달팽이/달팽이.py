# https://www.acmicpc.net/problem/1913

dir = [(1,0),(0,1),(-1,0),(0,-1)]

N = int(input())
T = int(input())

Num = N*N
ans = (N//2+1,N//2+1)
arr = [[0 for _ in range(N)] for _ in range(N)]
x,y = 0,0
didx = 0
while(Num>1):
    if (Num == T):
        ans = (y+1,x+1)
    arr[y][x] = Num
    ny,nx = y + dir[didx][0], x+ dir[didx][1]
    if 0 <= ny and ny < N and 0<= nx and nx < N and not arr[ny][nx]:
        x = nx
        y = ny
        Num -= 1
    else:
        didx = (didx+1) % 4 
arr[y][x] = 1
for _ in range(N):
    print(*arr[_])
print(*ans)