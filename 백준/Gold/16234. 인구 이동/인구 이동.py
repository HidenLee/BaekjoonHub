N, L, R = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(N)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]
day = 0
from collections import deque
while day <= 2000:
    visit = [[False] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            visit[i][j] = True
            count = 0
            dq = deque([(i,j)])
            union = set([(i,j)])
            while dq:
                ox, oy = dq.popleft()
                count += world[ox][oy]
                for dx, dy in delta:
                    nx, ny = ox + dx, oy + dy
                    if 0 <= nx < N and 0 <= ny < N and L <= abs(world[ox][oy]-world[nx][ny]) <= R and not visit[nx][ny]:
                        visit[nx][ny] = True
                        dq.append((nx,ny))
                        union.add((nx,ny))
            if len(union) >= 2:
                avr = count // len(union)
                for tx, ty in union:
                    world[tx][ty] = avr
                flag = False
    if flag:
        print(day)
        break
    day += 1