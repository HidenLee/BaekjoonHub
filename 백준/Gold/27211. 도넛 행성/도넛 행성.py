#https://www.acmicpc.net/problem/27211 도넛행성

def search(n,m):
    pass

delta = [(0,1),(1,0),(0,-1),(-1,0)]

N, M = map(int,input().split())
planet = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if not planet[i][j]:
            cnt += 1     
            stack = [(i,j)]
            while stack:
                oy, ox = stack.pop()
                if planet[oy][ox]:
                    continue

                planet[oy][ox] = 1
                for d in delta:
                    ny = (oy + d[0] + N ) % N
                    nx = (ox + d[1] + M ) % M
                    if not planet[ny][nx]:
                        stack.append((ny,nx))
print(cnt)
