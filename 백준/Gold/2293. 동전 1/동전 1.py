n, k = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])
dp = [0]*(k+1)
dp[0] = 1
# dp[arr[0]] = 1
for elm in arr:
    for i in range(arr[0],k+1):
        if i - elm >= 0:
            dp[i] += dp[i-elm]
# print(dp)
print(dp[k])