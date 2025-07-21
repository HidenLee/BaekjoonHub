from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    state = [[1]*m for _ in range(n)]
    delta = [(1,0),(0,1),(-1,0),(0,-1)]

    def update_air():
        air = set()
        visit = [[False]*m for _ in range(n)]
        dq = deque()

        for i in range(n):
            for j in range(m):
                if state[i][j] == 0 and (i in (0,n-1) or j in (0,m-1)):
                    dq.append((i,j))
                    air.add((i,j))
                    visit[i][j] = True

        while dq:
            y, x = dq.popleft()
            for dy, dx in delta:
                ny, nx = y+dy, x+dx
                if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx] and state[ny][nx] == 0:
                    visit[ny][nx] = True
                    air.add((ny,nx))
                    dq.append((ny,nx))
        return air

    for req in requests:
        air = update_air()
        for i in range(n):
            for j in range(m):
                if state[i][j] == 1 and storage[i][j] == req[0]:
                    if len(req) == 2:
                        state[i][j] = 0
                        continue
                    for dy, dx in delta:
                        ni, nj = i+dy, j+dx
                        if not (0 <= ni < n and 0 <= nj < m) or (ni, nj) in air:
                            state[i][j] = 0
                            break
                    else:
                        continue
                    
    return sum(map(sum, state))
