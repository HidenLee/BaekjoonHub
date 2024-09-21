N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

delta = [(1,0),(0,1),(-1,0),(0,-1)]
ans = 1
for height in range(1,100):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= height or visit[i][j]:
                continue
            stack = [(i,j)]
            while stack:
                oy,ox = stack.pop()
                visit[oy][ox] = True
                for dy,dx in delta:
                    ny,nx = oy+dy,dx+ox
                    if 0<=ny<N and 0<=nx<N and not visit[ny][nx] and arr[ny][nx] > height:
                        stack.append((ny,nx))
            cnt += 1
    # print(height,cnt)    
    ans = max(cnt,ans)
print(ans)