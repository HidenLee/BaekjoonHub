def solution(board):
    from collections import deque
    N = len(board)
    M = len(board[0])
    sx = sy = gx = gy = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                sy, sx = i,j
                continue
            if board[i][j] == "G":
                gy,gx = i,j
                continue
    answer = 0
    visit = {}
    dq = deque([(sy,sx,0)])
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    while dq:
        oy, ox, cost = dq.popleft()
        for dy, dx in delta:
            ny, nx = oy + dy , ox + dx
            while 0<= ny < N and 0<= nx < M:
                if board[ny][nx] == "D":
                    break
                ny += dy
                nx += dx
            ny -= dy
            nx -= dx
            if oy == ny and ox == nx:
                continue
            if ny == gy and nx == gx:
                return cost + 1
            if ny*M+nx not in visit or visit[ny*M+nx] > cost + 1:
                visit[ny*M+nx] = cost + 1
                dq.append((ny,nx,cost+1))
    return -1