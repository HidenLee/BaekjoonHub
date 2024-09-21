N = int(input())
delta = [(1,0),(0,1),(-1,0),(0,-1)]
arr = [list(input()) for _ in range(N)]
visit = [[False]* N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if visit[i][j] or arr[i][j] == "0":
            continue
        stack = [(i,j)]
        visit[i][j] = True
        size = 0
        while stack:
            oy,ox = stack.pop()
            size += 1
            for ny,nx in [(oy+dt[0],ox+dt[1]) for dt in delta]:
                if 0<=ny<N and 0<=nx<N and not visit[ny][nx] and  arr[ny][nx]=="1":
                    visit[ny][nx] = True
                    stack.append((ny,nx))
        ans.append(size)
print(len(ans))
ans.sort()
for _ in range(len(ans)):
    print(ans[_])