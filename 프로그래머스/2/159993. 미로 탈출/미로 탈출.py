def solution(maps):
    from collections import deque
    N = len(maps)
    M = len(maps[0])
    visit = [[N*M+1 for _ in range(M)] for _ in range(N)]
    
    def bfs(y,x,target):
        delta = [(1,0),(0,1),(-1,0),(0,-1)]
        visit = [[N*M+1 for _ in range(M)] for _ in range(N)]
        dq = deque([(y,x,0)])
        visit[y][x] = 0
        while dq:
            oy,ox,cost = dq.popleft()
            if maps[oy][ox] == target:
                if target == "E":
                    return cost
                phase2 = bfs(oy,ox,"E")
                return cost + phase2 if phase2 else 0 
            for ny,nx in [(dy+oy,dx+ox) for dy,dx in delta if 0<=dy+oy<N and 0<=dx+ox<M and maps[dy+oy][dx+ox] != "X"]:
                if visit[ny][nx] > visit[oy][ox] + 1:
                    visit[ny][nx] = visit[oy][ox] + 1
                    dq.append((ny,nx,visit[ny][nx]))    
        
        return 0
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "S":
                answer = bfs(i,j,"L")
                break
    return answer if answer else -1