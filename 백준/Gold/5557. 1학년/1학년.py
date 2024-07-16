
N = int(input())

arr = list(map(int,input().split()))
ans = 0

dp = [[0]*21 for _ in range(N)]
dp[0][arr[0]] = 1
for idx in range(1,N):
    new = arr[idx]
    for j in range(0,21):
        for nxt in (j+new, j-new):
            if 0 <= nxt <= 20:
                dp[idx][j] += dp[idx-1][nxt]

print(dp[N-2][arr[-1]])