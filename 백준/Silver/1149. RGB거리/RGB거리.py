table = [tuple(map(int,input().split())) for _ in range(int(input()))]
MAX_VALUE = 1000 * 1000 + 1
dp = [[MAX_VALUE]*3 for _ in range(len(table))]
dp[0] = table[0]
for i in range(1,len(table)):
    for j in range(3):
        dp[i][j] = min([dp[i-1][k] + table[i][j] for k in range(3) if k!=j])
print(min(dp[-1]))