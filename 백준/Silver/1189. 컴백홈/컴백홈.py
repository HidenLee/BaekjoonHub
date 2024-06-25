#https://www.acmicpc.net/problem/1189

delta = [(0,-1),(1,0),(0,1),(-1,0)]

R, C, K = map(int, input().split())
table = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
def backtracking(x,y,depth,cnt):
    visited[y][x] = True
    
    if depth == K :
        if y == 0 and x == C - 1:
            return cnt + 1
        return cnt
    for dt in delta:
        nx = x + dt[0]
        ny = y + dt[1]
        if 0<= nx < C and 0 <= ny < R and not visited[ny][nx] and table[ny][nx] != "T":
            visited[ny][nx] = True
            cnt = backtracking(nx,ny,depth+1,cnt)
            visited[ny][nx] = False
    return cnt

print(backtracking(0,R-1,1,0))