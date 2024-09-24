# https://www.acmicpc.net/problem/2146

delta = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(i,j):
    global islandIdx
    global arr

    stack = [(i,j)]
    history = [(i,j)]
    while stack:
        ox, oy  = stack.pop()
        arr[ox][oy] = islandIdx
        for nx,ny in [(ox+dx,oy+dy) for dx,dy in delta]:
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == "1":
                stack.append((nx,ny))
                history.append((nx,ny))
    islandIdx += 1
    
    for x, y in history:
        bfs(x,y)



from collections import deque
def bfs(i,j):
    global minDist
    deq = deque([(i,j,0)])
    visit = [[False]*N for _ in range(N)]
    visit[i][j] = True
    while deq:
        # print(deq)
        
        ox,oy,depth = deq.pop()
        for nx,ny in [(ox+dx,oy+dy) for dx,dy in delta]:
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                # print(i,j,nx,ny)

                if arr[nx][ny] == "1" and depth + 1 < minDist:
                    minDist = depth + 1
                    # print(arr)
                    return
                elif arr[nx][ny] == "0" and depth +1 <= minDist:
                    deq.appendleft((nx,ny,depth+1))
                    visit[nx][ny] = True
            

N = int(input())
arr = [list(input().split()) for _ in range(N)]

# N = 3
# arr = [["1","1","0"],["0","0","0"],["0","0","1"]]

# 일단 섬을 찾아 - 1일때 주변 1 완탐 - visited 대신에 섬index를 2~ 하나씩 올려
# 가장자리에서 bfs를 돌려서 1을 찾아, 길은 0뿐이야
islandIdx = 2
minDist = 10001

for i in range(N):
    for j in range(N):
        if arr[i][j] == "1":
            dfs(i,j)

# print(arr)
print(minDist-1)