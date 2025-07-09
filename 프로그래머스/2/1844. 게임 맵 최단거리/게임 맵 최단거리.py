def solution(maps):
    from collections import deque
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    n = len(maps)
    m = len(maps[0])
    visit = [[n*m+1 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    # visit[-1][-1] = -1
    
    dq = deque([(0,0)])
    while dq:
        oy, ox = dq.popleft()
        for dx, dy in delta:
            nx, ny = ox + dx, oy + dy
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] and visit[oy][ox] + 1 < visit[ny][nx]:
                visit[ny][nx] = visit[oy][ox] + 1
                dq.append((ny,nx))
                if ny == n-1 and nx == m-1:
                    return visit[ny][nx]
    return -1 if visit[-1][-1] == n*m+1 else visit[-1][-1]