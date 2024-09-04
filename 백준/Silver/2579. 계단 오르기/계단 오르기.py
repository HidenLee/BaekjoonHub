N = int(input())
arr = [ int(input()) for _ in range(N)]
arr = [0] + arr
dp = [0]*(N+1)
dp[0] = arr[0]
if N > 0:
    dp[1] = arr[1]
if N > 1:
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
for i in range(3,N+1):
    dp[i] = arr[i] + max(
        dp[i-2],
        dp[i-3] + arr[i-1]
    )
print(dp[N])