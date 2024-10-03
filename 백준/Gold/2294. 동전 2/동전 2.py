n, k = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])
maxV = 10**9
dp = [maxV]*(k+1)
dp[0] = 0
for i in range(arr[0],k+1):
    for coin in arr:
        if i - coin >= 0:
            dp[i] = min(dp[i],dp[i-coin]+1)

print(dp[k] if dp[k]!=maxV else -1)
