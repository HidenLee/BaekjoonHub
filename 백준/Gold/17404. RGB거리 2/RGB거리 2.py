table = [tuple(map(int,input().split())) for _ in range(int(input()))]
MAX_VALUE = 1000 * 1000 + 1
ans = MAX_VALUE
for l in range(3):
    dp = [[MAX_VALUE for _ in range(3)] for _ in range(len(table))]
    dp[0][l] = table[0][l]

    for i in range(1,len(table)):
        for j in range(3):
            dp[i][j] = min([dp[i-1][k] + table[i][j] for k in range(3) if k!=j])
    ans = min([ans]+[dp[len(table)-1][x] for x in range(3) if x!=l ])
print(ans)