# https://www.acmicpc.net/problem/17070 파이프옮기기1

# dp[y][x][d] 로 착안, 각 좌표에 특정 방향의 파이프 끝이 있는 경우를 dp로 연산
# 0 가로, 1 세로, 2 대각

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]    

dp[0][1][0] = 1

for i in range(2,N):
    if house[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1,N):
    for j in range(1,N):
        if house[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        
            if house[i][j-1] == 0 and house[i-1][j] == 0 and house[i-1][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
print(sum(dp[N-1][N-1]))