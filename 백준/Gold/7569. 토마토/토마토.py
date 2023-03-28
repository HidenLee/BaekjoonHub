from collections import deque
delta = [(0,0,1),(0,0,-1),(0,-1,0),(0,1,0),(1,0,0),(-1,0,0)]    

M, N, H = map(int,input().split())
array = [[] for _ in range(H)]
tomatoes = deque()
distance = [[[999]*M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for j in range(N):
        temp = list(map(int,input().split()))
        for i in range(M):
            if temp[i] != 0:
                distance[h][j][i] = 0
                if temp[i] == 1:
                    tomatoes.appendleft((i,j,h))
        array[h].append(temp)
        
        
while tomatoes:
    i,j,h = tomatoes.pop()
    for ni,nj,nh in [(i+dlt[0],j+dlt[1],h+dlt[2]) for dlt in delta if 0<=i+dlt[0]<M and 0<=j+dlt[1]<N and 0<=h+dlt[2]<H and not array[h+dlt[2]][j+dlt[1]][i+dlt[0]]]:
        tomatoes.appendleft((ni,nj,nh))
        array[nh][nj][ni] = array[h][j][i] + 1
rst = 0
for i,j,h in [(a,b,c) for a in range(M) for b in range(N) for c in range(H)]:
    if array[h][j][i] == 0:
        print(-1)
        break
    else:
        rst = max(array[h][j][i],rst)
else:
    print(rst-1)