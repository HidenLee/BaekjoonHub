# vhttps://www.acmicpc.net/problem/10844

n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][0] = 0
for idx in range(1,n):
    dp[idx][0] = dp[idx-1][1]
    dp[idx][9] = dp[idx-1][8]
    for jdx in range(1,9):
        dp[idx][jdx] = dp[idx-1][jdx-1] + dp[idx-1][jdx+1]
print(sum(dp[-1])%1000000000)