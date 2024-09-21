N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
# print(arr)
delta = [(0,1),(1,0),(0,-1),(-1,0)]
from collections import deque
deq = deque([(0,0)])
dist = [[N*M+1]*M for _ in range(N)]
dist[0][0] = 1
while deq:
    ox, oy = deq.pop()
    for dx,dy in delta:
        nx, ny = dx+ox, dy+oy
        if 0<=nx<M and 0<=ny<N and arr[ny][nx] == "1":
            if dist[ny][nx] > dist[oy][ox] + 1:
                dist[ny][nx] = dist[oy][ox] + 1
                deq.appendleft((nx,ny))
print(dist[-1][-1])

