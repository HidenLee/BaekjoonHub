from bisect import bisect_left
N = int(input())
arr = [-1001] + list(map(lambda x : -int(x),input().split()))
dp = [1001] * (N+1)
ans = 0
for idx in range(1,N+1):
    jdx = bisect_left(dp,arr[idx])
    ans = max(jdx,ans)
    dp[jdx] = arr[idx]
print(ans+1)
