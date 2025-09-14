N,M = map(int,input().split())
a,b,c = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(N)]

pre_sum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    prev = 0
    for j in range(M):
        prev += table[i][j]
        pre_sum[i+1][j+1] = pre_sum[i][j+1] + prev
minV = float('inf')

def pre_2d(y1,x1,y2,x2):
    return pre_sum[y2][x2] - pre_sum[y1][x2] - pre_sum[y2][x1] + pre_sum[y1][x1]

for i in range(N):
    for j in range(M):
        if i + a <= N and j + b + c <= M:
            minV = min(minV,pre_2d(i,j,i+a,j+b+c))
        if i + a + c <= N and j + b + a <= M:
            minV = min(minV,pre_2d(i,j,i+a,j+b) + pre_2d(i+a,j+b,i+a+c,j+b+a))
        if i + a + b <= N and j + c + a <= M:
            minV = min(minV,pre_2d(i,j,i+a,j+c) + pre_2d(i+a,j+c,i+a+b,j+c+a))      
print(minV)

