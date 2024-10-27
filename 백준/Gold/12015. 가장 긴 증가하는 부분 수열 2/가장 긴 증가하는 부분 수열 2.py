from bisect import bisect_left
N = int(input())
arr = [0] + list(map(int,input().split()))
dp = [10000000] * (N+1)
ans = 0
for idx in range(1,N+1):
    jdx = bisect_left(dp,arr[idx])
    ans = max(jdx,ans)
    dp[jdx] = arr[idx]
print(ans+1)
