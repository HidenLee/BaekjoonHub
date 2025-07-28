def solution(land):
    n = len(land)
    m = len(land[0])
    answer = [0 for _ in range(m)]
    visit = [[False for _ in range(m)] for _ in range(n)]
    flag = 0
    
    delta = [[1,0],[0,1],[-1,0],[0,-1]]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visit[i][j]:
                xset = set()
                count = 0
                stack = [(i,j)]
                visit[i][j] = True
                while stack:
                    oy, ox = stack.pop()
                    xset.add(ox)
                    count += 1
                    for ny, nx in [(oy+dy,ox+dx) for dy,dx in delta if 0<=oy+dy<n and 0<=ox+dx<m]:
                        if land[ny][nx] == 1 and not visit[ny][nx]:
                            visit[ny][nx] = True
                            stack.append((ny,nx))
                for x in xset:
                    answer[x] += count
                    
    return max(answer)