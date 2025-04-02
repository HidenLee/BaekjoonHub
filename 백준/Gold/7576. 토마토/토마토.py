from collections import deque

M, N = map(int,input().split())
flag = False
dq = deque([])
delta = [(0,1),(1,0),(0,-1),(-1,0)]
table = []
for _ in range(N):
    ipt = list(map(int,input().split()))
    for idx,elm in enumerate(ipt):
        if elm == 0:
            flag = True
            ipt[idx] = 0
        if elm == 1:
            dq.append((_,idx))
    table.append(ipt)
if not flag:
    print(0)
    exit()

while dq:
    oy,ox = dq.popleft()
    for ny, nx in [(oy+dt[0],ox+dt[1]) for dt in delta if 0<=oy+dt[0]<N and 0<=ox+dt[1]<M]:
        if table[ny][nx] == 0 :
            table[ny][nx] = table[oy][ox] + 1
            dq.append((ny,nx))
answer = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer, table[i][j])
print(answer-1)