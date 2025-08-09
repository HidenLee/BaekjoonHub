def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    visit = [[False for _ in range(M)] for _ in range(N)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] or maps[i][j] == "X":
                continue
            stack = [(i,j)]
            visit[i][j] = True
            count = 0
            while stack:
                oy,ox = stack.pop()
                count += int(maps[oy][ox])
                for dy,dx in delta:
                    ny,nx = oy+dy,ox+dx
                    if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx] and maps[ny][nx] != "X":
                        stack.append((ny,nx))
                        visit[ny][nx] = True
            if count:
                answer.append(count)
    return sorted(answer) if answer else [-1]