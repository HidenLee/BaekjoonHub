def solution(grid):
    def delta(n):
        return[(0,1),(1,0),(0,-1),(-1,0)][n%4]
    N = len(grid)
    M = len(grid[0])
    visit = [[False for _ in range(4)] for _ in range(N*M)]
    answer = []
    for start in range(N*M):
        oy, ox = divmod(start,M)
        for arrow in range(4):
            if visit[start][arrow]:
                continue
            ny, nx = oy, ox
            nxt_arrow = arrow
            count = 0
            stack = []
            while not visit[ny*M+nx][nxt_arrow%4]:
                visit[ny*M+nx][nxt_arrow%4] = True
                dy ,dx = delta(nxt_arrow)
                ny, nx = (ny+dy)%N, (nx+dx)%M
                node = grid[ny][nx]
                nxt_arrow += 1 if node == "R" else 0 if node  == "S" else 3 
                count += 1
            answer.append(count)
            
    return sorted(answer)